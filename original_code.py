#this is the original code I submitted for the test. 

def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return ('Error: Too many problems.')
        

    # list of all operations in str format
    #shows error message when not '-' or '+'
    operations = list(map(lambda x: x.split()[1], problems))
    if set(operations) != {'+', '-'} and len(set(operations)) != 2:  #there is a mistake in this lane that prevents TEST 9 to pass. 
         return ("Error: Operator must be '+' or '-'.")

    numbers = []  # list of all operands in str format
    for i in problems:
        p = i.split()
        numbers.extend([p[0], p[2]])

    if not all(map(lambda x: x.isdigit(), numbers)):
        
        return ('Error: Numbers must only contain digits.')

    if not all(map(lambda x: len(x) < 5, numbers)):
        
        return ('Error: Numbers cannot be more than four digits.')

    top_row = ''
    dashes = ''
    values = list(map(lambda x: eval(x), problems))
    solutions = ''
    for i in range(0, len(numbers), 2):
        space_width = max(len(numbers[i]), len(numbers[i+1])) + 2
        top_row += numbers[i].rjust(space_width)
        dashes += '-' * space_width
        solutions += str(values[i // 2]).rjust(space_width)
        if i != len(numbers) - 2:
            top_row += ' ' * 4
            dashes += ' ' * 4
            solutions += ' ' * 4

    bottom_row = ''
    for i in range(1, len(numbers), 2):
        space_width = max(len(numbers[i - 1]), len(numbers[i])) + 1
        bottom_row += operations[i // 2]
        bottom_row += numbers[i].rjust(space_width)
        if i != len(numbers) - 1:
            bottom_row += ' ' * 4

    if show_answers:
        problems = '\n'.join((top_row, bottom_row, dashes, solutions))
    else:
        problems = '\n'.join((top_row, bottom_row, dashes))
    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

print(f'\n{arithmetic_arranger(["3 + 855", "988 + 10"])}') #testing parameter 9 -not working regardless of operator meeting conditions.
