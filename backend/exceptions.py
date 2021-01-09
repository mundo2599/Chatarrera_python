class Exceptions:
    NO_PARAMETERS = ValueError('No parameters provided')
    MATERIAL_NO_EXISTS = ValueError("Material provided doesn't exit")
    PARENT_NO_EXISTS = ValueError("Parent provided doesn't exit")
    VALUE_LESS_ZERO = ValueError("Value can not be less than zero")
    MATERIAL_EXISTS = ValueError("Material provided already exists")
    CHILD_NO_VALID = ValueError("Material provided is child, parent required")