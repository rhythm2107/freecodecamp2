import re

test_list = ["32 + 69", "3801 - 2", "45 + 43", "123 + 49"]

def arithmetic_arrange(list, solver=False):
    extracted_numbers = []
    # Takes care of lists longer than 5 problems
    if len(list) > 5:
        print('Error: Too many problems.')
        
    # Takes care of lists trying to use multiplication or division
    for problem in test_list:
        if problem.count('*') > 0 or problem.count('/') > 0:
            print("Error: Operator must be '+' or '-'.")
        
        # Takes care of lists trying to input [A-Z] instead of digits, might need to make this not work for other signs as well
        regex_AZ = re.findall("[A-Za-z]", problem)
        if regex_AZ:
            print("Error: Numbers must only contain digits.")

    # Takes care of numbers being longer than four digits.
    for item in test_list:
    # Extract each number using a more direct approach
        numbers = [int(num) for num in item.split() if num.isdigit() and len(num) > 4]
        extracted_numbers.extend(numbers)
    if extracted_numbers:
        print('Error: Numbers cannot be more than four digits.')



arithmetic_arrange(test_list)