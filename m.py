# ============================================================
# M- Programming Language
# Version 1.0
# ============================================================

import ast
import operator
import sys


# ============================================================
# OPERATORS
# ============================================================

BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

COMPARISON_OPERATORS = {
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.Lt: operator.lt,
    ast.LtE: operator.le,
    ast.Gt: operator.gt,
    ast.GtE: operator.ge,
}


# ============================================================
# M- FUNCTIONS
# ============================================================

functions = {}


# ============================================================
# EXPRESSION EVALUATOR
# ============================================================

def evaluate(expression, variables):
    expression = expression.strip()

    # String
    if (
        len(expression) >= 2
        and expression[0] == '"'
        and expression[-1] == '"'
    ):
        return expression[1:-1]

    # Boolean
    if expression == "true":
        return True

    if expression == "false":
        return False

    # Input
    if expression.startswith("Write(Enter ") and expression.endswith(")"):
        question = expression[12:-1]
        return input(question + ": ")

    # Variable
    if expression in variables:
        return variables[expression]

    # Integer / decimal
    try:
        if "." in expression:
            return float(expression)
        return int(expression)
    except ValueError:
        pass

    # Expression
    try:
        tree = ast.parse(expression, mode="eval")
        return evaluate_ast(tree.body, variables)
    except Exception as error:
        raise ValueError(
            f'Cannot evaluate "{expression}"'
        ) from error


def evaluate_ast(node, variables):

    # Numbers / strings
    if isinstance(node, ast.Constant):
        return node.value

    # Variables
    if isinstance(node, ast.Name):
        if node.id in variables:
            return variables[node.id]

        raise ValueError(
            f'Unknown variable "{node.id}"'
        )

    # Math
    if isinstance(node, ast.BinOp):

        operation = BINARY_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Unsupported operator")

        left = evaluate_ast(node.left, variables)
        right = evaluate_ast(node.right, variables)

        return operation(left, right)

    # Comparisons
    if isinstance(node, ast.Compare):

        left = evaluate_ast(node.left, variables)

        for op, comparator in zip(
            node.ops,
            node.comparators
        ):

            right = evaluate_ast(
                comparator,
                variables
            )

            operation = COMPARISON_OPERATORS.get(
                type(op)
            )

            if operation is None:
                raise ValueError(
                    "Unsupported comparison"
                )

            if not operation(left, right):
                return False

            left = right

        return True

    # AND / OR
    if isinstance(node, ast.BoolOp):

        values = [
            evaluate_ast(value, variables)
            for value in node.values
        ]

        if isinstance(node.op, ast.And):
            return all(values)

        if isinstance(node.op, ast.Or):
            return any(values)

    # NOT
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.Not):
            return not evaluate_ast(
                node.operand,
                variables
            )

        if isinstance(node.op, ast.USub):
            return -evaluate_ast(
                node.operand,
                variables
            )

    raise ValueError("Unsupported expression")


# ============================================================
# BLOCK READER
# ============================================================

def get_block(lines, start):

    block = []
    depth = 1
    index = start + 1

    while index < len(lines):

        line = lines[index].strip()

        if line.endswith("{"):
            depth += 1

        if line == "}":
            depth -= 1

            if depth == 0:
                return block, index

        block.append(lines[index])

        index += 1

    raise ValueError(
        "Missing closing '}'"
    )


# ============================================================
# M- INTERPRETER
# ============================================================

def execute(lines, variables=None):

    if variables is None:
        variables = {}

    index = 0

    while index < len(lines):

        raw_line = lines[index]
        line = raw_line.strip()

        # Ignore blank lines
        if not line:
            index += 1
            continue

        # Ignore comments
        if line.startswith("#"):
            index += 1
            continue

        # ----------------------------------------------------
        # SAVE
        # ----------------------------------------------------

        if line.startswith("Save "):

            command = line[5:]

            if "=" not in command:
                raise ValueError(
                    f"Line {index + 1}: Save requires '='"
                )

            name, expression = command.split(
                "=",
                1
            )

            name = name.strip()
            expression = expression.strip()

            if not name.replace("_", "").isalnum():
                raise ValueError(
                    f'Invalid variable name "{name}"'
                )

            variables[name] = evaluate(
                expression,
                variables
            )

            index += 1
            continue

        # ----------------------------------------------------
        # WRITE
        # ----------------------------------------------------

        if (
            line.startswith("Write(")
            and line.endswith(")")
        ):

            expression = line[6:-1].strip()

            result = evaluate(
                expression,
                variables
            )

            print(result)

            index += 1
            continue

        # ----------------------------------------------------
        # IF
        # ----------------------------------------------------

        if line.startswith("If ") and line.endswith("{"):

            condition = line[3:-1].strip()

            block, end = get_block(
                lines,
                index
            )

            if evaluate(
                condition,
                variables
            ):
                execute(
                    block,
                    variables
                )

            index = end + 1

            # ELSE
            if (
                index < len(lines)
                and lines[index].strip() == "Else {"
            ):

                else_block, else_end = get_block(
                    lines,
                    index
                )

                if not evaluate(
                    condition,
                    variables
                ):
                    execute(
                        else_block,
                        variables
                    )

                index = else_end + 1

            continue

        # ----------------------------------------------------
        # REPEAT
        # ----------------------------------------------------

        if (
            line.startswith("Repeat ")
            and line.endswith("{")
        ):

            expression = line[7:-1].strip()

            count = int(
                evaluate(
                    expression,
                    variables
                )
            )

            block, end = get_block(
                lines,
                index
            )

            for _ in range(count):
                execute(
                    block,
                    variables
                )

            index = end + 1
            continue

        # ----------------------------------------------------
        # WHILE
        # ----------------------------------------------------

        if (
            line.startswith("While ")
            and line.endswith("{")
        ):

            condition = line[6:-1].strip()

            block, end = get_block(
                lines,
                index
            )

            safety = 0

            while evaluate(
                condition,
                variables
            ):

                execute(
                    block,
                    variables
                )

                safety += 1

                if safety > 100000:
                    raise RuntimeError(
                        "Possible infinite loop"
                    )

            index = end + 1
            continue

        # ----------------------------------------------------
        # FUNCTION
        # ----------------------------------------------------

        if (
            line.startswith("Function ")
            and line.endswith("{")
        ):

            declaration = line[9:-1].strip()

            name = declaration.split("(")[0].strip()

            parameter_text = declaration[
                declaration.find("(") + 1:
                declaration.rfind(")")
            ]

            parameters = []

            if parameter_text.strip():
                parameters = [
                    p.strip()
                    for p in parameter_text.split(",")
                ]

            block, end = get_block(
                lines,
                index
            )

            functions[name] = {
                "parameters": parameters,
                "body": block
            }

            index = end + 1
            continue

        # ----------------------------------------------------
        # FUNCTION CALL
        # ----------------------------------------------------

        if "(" in line and line.endswith(")"):

            name = line.split("(")[0].strip()

            if name in functions:

                arguments_text = line[
                    line.find("(") + 1:
                    line.rfind(")")
                ]

                arguments = []

                if arguments_text.strip():

                    arguments = [
                        evaluate(
                            argument.strip(),
                            variables
                        )
                        for argument
                        in arguments_text.split(",")
                    ]

                function = functions[name]

                local_variables = variables.copy()

                for parameter, argument in zip(
                    function["parameters"],
                    arguments
                ):
                    local_variables[
                        parameter
                    ] = argument

                execute(
                    function["body"],
                    local_variables
                )

                index += 1
                continue

        # ----------------------------------------------------
        # UNKNOWN COMMAND
        # ----------------------------------------------------

        raise ValueError(
            f'Line {index + 1}: '
            f'Unknown M- command "{line}"'
        )

    return variables


# ============================================================
# M- STARTUP
# ============================================================

def main():

    print("M- Programming Language")
    print("Version 1.0")
    print("------------------------")

    filename = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "program.m"
    )

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as file:

            code = file.read()

        lines = code.splitlines()

        execute(lines)

    except FileNotFoundError:

        print(
            f'M- Error: File "{filename}" not found.'
        )

    except Exception as error:

        print(
            "M- Error:",
            error
        )


if __name__ == "__main__":
    main()
