keywords = ['False', 'await', 'else', 'import', 'pass', 'None', 'break', 'except', 'in',
            'raise', 'True', 'class', 'finally', 'is', 'return', 'and', 'continue', 'for',
            'lambda', 'try', 'as', 'def', 'from', 'nonlocal', 'while', 'assert', 'del',
            'global', 'not', 'with', 'async', 'elif', 'if', 'or', 'yield']


def is_valid_variable_name(var_name):
    # Check if the name is a Python keyword
    if var_name in keywords:
        return False, f"'{var_name}' is a reserved keyword"

    # Check if the name starts with a valid character (letter or underscore)
    if not (var_name[0].isalpha() or var_name[0] == '_'):
        return False, f"'{var_name}' is invalid because it must start with a letter or underscore"

    # Check if all characters are valid (letters, numbers, or underscore)
    for char in var_name:
        if not (char.isalnum() or char == '_'):
            return False, f"'{var_name}' contains invalid character '{char}'"

    # If all checks pass, the variable name is valid
    return True, f"'{var_name}' is a valid variable name"
