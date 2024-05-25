from dataclasses import dataclass
from enum import Enum
import importlib
import re
from typing import Any, Optional


class JSONSchemaType(str, Enum):
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    OBJECT = "object"
    ARRAY = "array"
    BOOLEAN = "boolean"
    NULL = "null"


@dataclass
class Property:
    name: str
    schema_type: JSONSchemaType | None
    description: str
    item_type: JSONSchemaType | None = None
    enum: list[str | int] | None = None
    
    def serialize(self):
        base =  {
            "type": self.schema_type.value,
            "description": self.description,
        }
        if self.enum:
            base["enum"] = self.enum
        
        if self.schema_type == JSONSchemaType.ARRAY:
            if self.item_type is None:
                raise ValueError("Must specify `item_type` for the `ARRAY` JSON schema type!")
            base["items"] = {"type": self.item_type.value}
        return base


@dataclass
class FunctionParameters:
    properties: list[Property]
    required: list[str]
    type: str = "object"

    def serialize(self) -> dict[str, str | dict[str, Any] | list[str]]:
        base = {"type": self.type, "properties": {}, "required": self.required}
        for p in self.properties:
            base["properties"][p.name] = p.serialize()
        return base
    
    def property_exists(self, prop_name) -> Property | None:
        for p in self.properties:
            if p.name == prop_name:
                return p
        return None


@dataclass
class FunctionSpec:
    name: str
    description: str
    params: FunctionParameters

    def serialize(self) -> dict[str, str | dict[str, Any]]:
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.params.serialize()
            }
        }


def convert_type_to_json_schema(inputted_type: Any) -> JSONSchemaType:
    schema_types = [x.value for x in JSONSchemaType]
    if inputted_type in schema_types:
        return inputted_type
    match inputted_type:
        case "str":
            return JSONSchemaType.STRING
        case "int":
            return JSONSchemaType.INTEGER
        case "float":
            return JSONSchemaType.NUMBER
        case "bool":
            return JSONSchemaType.BOOLEAN
        case "None":
            return JSONSchemaType.NULL
    if re.findall(r"^list\[.+\]$", inputted_type):
        return JSONSchemaType.ARRAY
    raise ValueError(
        f"unrecognized type `{inputted_type}`...must be one of the following: `str`, `int`, `float`, `list[...]`, `bool`, `None`, " + 
        ", ".join(['`' + x.value + '`' for x in JSONSchemaType])
    )


def _handle_param(
    param_name: str,
    param_description: str,
    function_params: FunctionParameters,
) -> FunctionParameters:
    # Remove the `defaults to` from the description. Not totally necessary,
    # but whatever...
    defaults_to_regex = re.compile(', defaults to (.+)$')
    no_default_param_desc = re.sub(defaults_to_regex, "", param_description)

    # Add to properties
    prop = Property(
        name=param_name,
        schema_type=None,
        description=no_default_param_desc,
    )
    function_params.properties.append(prop)

    # Add to required
    has_default = re.findall(defaults_to_regex, param_description)
    if not has_default:
        function_params.required.append(param_name)

    return function_params


def _handle_type(
    param_name: str,
    type_description: str,
    function_params: FunctionParameters,
) -> FunctionParameters:
    # Check if the param type is an enum
    enum_values = []
    class_regex = re.compile('^class\s?:\s?(`[a-zA-Z\.]+`).*$')
    class_matches = re.findall(class_regex, type_description)
    if len(class_matches) > 1:
        raise ValueError(f"too many class types for `:type {param_name}:`")
    
    #TODO: this seems unsafe...
    if class_matches:

        # Grab the Enum class from the module that it lives within
        class_import_path = class_matches[0].strip().replace("`", "")
        split = class_import_path.split(".")
        module = importlib.import_module(".".join(split[:-1]))
        enum_cls = getattr(module, split[-1])
        if not enum_cls:
            raise ValueError(f"could not find Enum class {class_matches[0].strip()}")

        # Enum values
        enum_values = [x.value for x in enum_cls]
        if not enum_values:
            raise ValueError(f"could not find values for {enum_cls}...are you sure you specified the Enum correctly?")
        type_description = enum_values[0].__class__.__name__

    # Remove the `, optional` portion from the param type
    optional_regex = re.compile(', optional')
    param_type = re.sub(optional_regex, "", type_description)

    # If we've encountered a type before encountering the associated
    # param, raise an error
    prop = function_params.property_exists(param_name)
    if not prop:
        raise ValueError(f"encountered `:type {param_name}:` before `:param {param_name}:`")
    assert prop is not None

    # Set property type and enum values
    prop.schema_type = convert_type_to_json_schema(param_type)
    item_types = re.findall(r"list\[(.+)\]", param_type)
    if item_types:
        if len(item_types) > 1:
            raise ValueError(f"Too many item types! {item_types}")
        item_type = convert_type_to_json_schema(item_types[0])
        prop.item_type = item_type

    if enum_values:
        prop.enum = enum_values
    
    return function_params


def _handle_param_or_type(
    param_name: str,
    content: list[str],
    function_params: FunctionParameters,
    handling_param: bool,
    handling_type: bool,
) -> FunctionParameters:
    full_param_type_desc = " ".join(filter(None, content))

    # Handle param
    if handling_param:
        function_params = _handle_param(
            param_name=param_name,
            param_description=full_param_type_desc,
            function_params=function_params,
        )
    
    # Handle type
    if handling_type:
        function_params = _handle_type(
            param_name=param_name,
            type_description=full_param_type_desc,
            function_params=function_params
        )

    return function_params
    

def get_properties_from_docstring(
    function_name: str,
    docstring: str,
) -> FunctionSpec:
    tool_description: list[str] = []
    function_params = FunctionParameters(
        properties=[],
        required=[]
    )

    # Regexes
    param_regex = re.compile('^:param\s([a-zA-Z0-9_]+):(.+)(?:, defaults to (.+))?$')
    type_regex = re.compile('^:type\s([a-zA-Z0-9_]+):(.+)(?:, optional)?$')

    # Split docstring
    handling_param_name: Optional[str] = None
    handling_param: bool = False
    handling_type: bool = False
    handling_content: dict[str, list[str]] = {}
    for line in docstring.split("\n"):
        line = line.strip()

        # Find all matches to :param: and :type:. If they don't exist, then we're
        # still in the summary
        param_matches = re.findall(param_regex, line)
        type_matches = re.findall(type_regex, line)
        if len(param_matches) > 1 or len(type_matches) > 1:
            raise ValueError(f"Error in Sphinx docstring in line: `{line}`")

        # Check if we're currently handling a param or a type. If we are
        # and `param_matches` or `type_matches` is non-zero, then that
        # means our match is the *next* param / type.
        if handling_param or handling_type:

            # We have reached the *next* param / type
            if param_matches or type_matches:
                # Handling previous param or type
                function_params = _handle_param_or_type(
                    param_name=handling_param_name,
                    content=handling_content[handling_param_name],
                    function_params=function_params,
                    handling_param=handling_param,
                    handling_type=handling_type,
                )
                               
                # Okay, so we have handled the previous param and type matches. Now, we need to set
                # the initial value of the handling content
                handling_param = bool(param_matches)
                handling_type = bool(type_matches)
                matches_iterable = param_matches if param_matches else type_matches
    
                # Set the initial value of the handling content to be the description.
                # This gets appended as we iterate through the lines until we encounter
                # the next param or type
                match = matches_iterable[0]
                param_name = match[0].strip()
                param_type_description = match[1].strip()
                handling_param_name = param_name
                handling_content[param_name] = [param_type_description]

            else:
                handling_content[param_name].append(line)

        # We're not currently handling a param or a type.
        else:
            if not param_matches or type_matches:
                tool_description.append(line)
                continue

            # In this case, we've likely encountered the first :param: specification.
            handling_param = bool(param_matches)
            handling_type = bool(type_matches)
            matches_iterable = param_matches if param_matches else type_matches

            # Set the initial value of the handling content to be the description.
            # This gets appended as we iterate through the lines until we encounter
            # the next param or type
            match = matches_iterable[0]
            param_name = match[0].strip()
            param_type_description = match[1].strip()
            handling_param_name = param_name
            handling_content[param_name] = [param_type_description]

    # Handle stragglers
    function_params = _handle_param_or_type(
        param_name=handling_param_name,
        content=handling_content[handling_param_name],
        function_params=function_params,
        handling_param=handling_param,
        handling_type=handling_type,
    )

    # Build full spec
    spec = FunctionSpec(
        name=function_name,
        description=" ".join(tool_description).strip(),
        params=function_params
    )
    return spec
