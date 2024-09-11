from variable_name_checker import is_valid_variable_name


def syntax_checker(file_path):
    # Define basic keywords that should be followed by a colon
    keywords_with_colon = ['if', 'elif', 'else', 'for', 'while', 'def', 'class', 'try', 'except']

    # Open the file and read lines
    with open(file_path, 'r') as f:
        lines = f.readlines()

    indent_stack = []
    open_parens = 0
    error_list = []

    # Check each line for basic syntax issues
    for i, line in enumerate(lines, 1):
        stripped_line = line.strip()

        # Skip empty lines
        if not stripped_line:
            continue

        # Check for balanced parentheses ()
        open_parens += stripped_line.count('(') - stripped_line.count(')')
        if open_parens != 0:
            error_list.append(f"Error: Unmatched opening or closing parenthesis on line {i}")

        # Check for balanced curly braces {}
        open_parens += stripped_line.count('{') - stripped_line.count('}')
        if open_parens != 0:
            error_list.append(f"Error: Unmatched opening or closing curly brace on line {i}")

        # Check for balanced square brackets []
        open_parens += stripped_line.count('[') - stripped_line.count(']')
        if open_parens != 0:
            error_list.append(f"Error: Unmatched opening or closing square bracket on line {i}")

        # Check for basic indentation (assumes 4 spaces for simplicity)
        current_indent = len(line) - len(stripped_line)
        if current_indent == 1:
            current_indent = 0  # set the indentation to 0

        # Handle indentation changes
        if indent_stack and current_indent < indent_stack[-1]:
            while indent_stack and current_indent < indent_stack[-1]:
                indent_stack.pop()
                print(indent_stack)

        # Simple check for missing colons
        if any(stripped_line.startswith(keyword) for keyword in keywords_with_colon) and not stripped_line.endswith(
                ':'):
            error_list.append(f"Error: Missing colon after '{stripped_line.split()[0]}' on line {i}")

        # Indentation increase after colon
        if stripped_line.endswith(':'):
            if len(lines) < i+1:
                current_indent = (len(lines[i+1]) - len(lines[i+1].strip()))
            else:
                current_indent = (len(lines[i]) - len(lines[i].strip()))


            print(f"{current_indent} {len(line)} ,{len(stripped_line)}")
            indent_stack.append(current_indent)
            # current_indent = indent_stack[-1]
            # print(f"{indent_stack}")

        # Check if current indentation level matches the expected level
        if indent_stack and current_indent != indent_stack[-1]:
            error_list.append(f"Error: Incorrect indentation on line {i} indent stack {indent_stack} current indent {current_indent} indent {indent_stack[-1]}")

    for i, line in enumerate(lines, 1):
        # Split each line into words
        words = line.split()
        # Check each word if it's a valid variable name
        for word in words:
            # Let's assume the first word before "=" is the variable name (simplified logic)
            if '=' in word:
                var_name = word.split('=')[0]
                is_valid, message = is_valid_variable_name(var_name.strip())
                print(f"Line {i}: {message}")

    # Display the errors
    if not error_list:
        print("""
        -------------------------------------------------
        File Accepted
        No errors Found
        -------------------------------------------------
        """)
    else:
        print("------------------------------------------")
        print("File Rejected")
        for error in error_list:
            print(error)
        print("------------------------------------------")
