import re

test_list = ["3801 - 2", "123 + 49"]

def arithmetic_arranger(list, solver=False):
    
    # Takes care of lists longer than 5 problems
    if len(list) > 5:
        return 'Error: Too many problems.'
        
    # Takes care of lists trying to use multiplication or division
    for problem in list:
        if problem.count('*') > 0 or problem.count('/') > 0:
            return "Error: Operator must be '+' or '-'."
        
        # Takes care of lists trying to input [A-Z] instead of digits, might need to make this not work for other signs as well
        regex_AZ = re.findall("[A-Za-z]", problem)
        if regex_AZ:
            return "Error: Numbers must only contain digits."

    # Takes care of numbers being longer than four digits.
    extracted_numbers = []
    for item in list:
        numbers = [int(num) for num in item.split() if num.isdigit() and len(num) > 4]
        extracted_numbers.extend(numbers)
    if extracted_numbers:
        return "Error: Numbers cannot be more than four digits."

    output_list = []
    for item in list:
        # Split the item into numbers and operand using regular expression
        match = re.search(r"(\d+)\s+([\+\-])\s+(\d+)", item)
        if match:
            # Extract the numbers and operand from the match object
            num1, operand, num2 = match.groups()
            # Convert the numbers to integers
            num1 = int(num1)
            num2 = int(num2)
            # Create the tuple and append it to the output list
            output_list.append((num1, operand, num2))
        else:
            print(f"Error: Invalid expression: {item}")

    length = 6
    solution = 0
    top_line = ''
    middle_line = ''
    dash_line = ''
    solution_line = ''

    for tuple in output_list:
        first_num = tuple[0]
        operator = tuple[1]
        second_num = tuple[2]

        # Getting solution
        if operator == '+':
            solution = first_num + second_num
        elif operator == '-':
            solution = first_num - second_num

        # Getting dash count/width
        length = 2 + max(len(str(first_num)), len(str(second_num)))
        #print('Length:', length)

        #print(str(first_num).rjust(length))
        #print(str(operator), str(second_num).rjust(length-2))
        #print('-' * length)

        top_line += f"{str(first_num).rjust(length)}{' '*4}"
        middle_line += f"{operator} {str(second_num).rjust(length-2)}{' '*4}"
        dash_line += f"{'-' * length}{' '*4}"
        solution_line += f"{str(solution).rjust(length)}{' '*4}"
    
    if solver == False:
        return (f'{top_line.rstrip()}\n{middle_line.rstrip()}\n{dash_line.rstrip()}')
    if solver == True:
        return (f'{top_line.rstrip()}\n{middle_line.rstrip()}\n{dash_line.rstrip()}\n{solution_line.rstrip()}')