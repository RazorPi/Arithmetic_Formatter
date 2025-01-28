#This is the final code that PASSED all TESTS. The construct is different from the original; it is a combination of ChatGPT code + research. 

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    top_row = ""
    bottom_row = ""
    dashes = ""
    solutions = ""

    for index, problem in enumerate(problems):
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Determine width
        width = max(len(num1), len(num2)) + 2

        # Format lines
        top_row += num1.rjust(width)
        bottom_row += operator + num2.rjust(width - 1)
        dashes += "-" * width
        if show_answers:
            solution = str(eval(num1 + operator + num2))  # Safe evaluation
            solutions += solution.rjust(width)

        # Add spacing between problems
        if index < len(problems) - 1:
            top_row += "    "
            bottom_row += "    "
            dashes += "    "
            solutions += "    "

    # Construct final output
    if show_answers:
        return f"{top_row}\n{bottom_row}\n{dashes}\n{solutions}"
    else:
        return f"{top_row}\n{bottom_row}\n{dashes}"


# Test example
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
