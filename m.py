# M- Programming Language
# Version 0.1

def get_value(value, variables):
    value = value.strip()

    # Text
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]

    # Number
    try:
        return int(value)
    except ValueError:
        pass

    # Variable
    if value in variables:
        return variables[value]

    return value


def run_m(code):
    variables = {}

    for line in code.splitlines():
        line = line.strip()

        # Ignore empty lines and comments
        if not line or line.startswith("#"):
            continue

        # Save
        if line.startswith("Save "):
            command = line[5:]

            if "=" not in command:
                print("M- Error: Save needs '='")
                continue

            name, value = command.split("=", 1)

            name = name.strip()
            value = value.strip()

            variables[name] = get_value(value, variables)

        # Write
        elif line.startswith("Write(") and line.endswith(")"):
            value = line[6:-1].strip()

            # Variable
            if value in variables:
                print(variables[value])

            # Text
            elif value.startswith('"') and value.endswith('"'):
                print(value[1:-1])

            else:
                print(value)

        else:
            print("M- Error: Unknown command -> " + line)


# Load M- program
try:
    with open("program.m", "r") as file:
        code = file.read()

    run_m(code)

except FileNotFoundError:
    print("M- Error: program.m was not found.")
