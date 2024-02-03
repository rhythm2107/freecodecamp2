def convert_to_int_array(number_string):
    # Converts a string of digits only to an array
    if not number_string.isdigit():
        return None # Handles invalid input
    else:
        return [int(digit) for digit in number_string]

def verify_card_number(card_number):
    card_number_reversed = card_number[::-1] # Reversing order of credit card number
    odd_result = 0
    even_result = 0
    
    # Iterating through card_number_reversed, retrieving arrays of even & odd numbers
    for digit in card_number_reversed:
        odd_digits = card_number_reversed[0::2]
        even_digits = card_number_reversed[1::2]
        odd_array = convert_to_int_array(odd_digits)
        even_array = convert_to_int_array(even_digits)
    
    for number in odd_array:
        odd_result += number

    for number2 in even_array:
        temp_result = (number2 * 2)
        if temp_result >= 10 :
            temp_result_str = str(temp_result)
            even_result_1 = (int(temp_result_str[0]) + int(temp_result_str[1]))
        else:
            even_result += temp_result

    even_result += even_result_1
    final_result = even_result + odd_result
    if int(final_result) % 10 == 0 :
        print('Credit card number is valid!')
    else:
        print('Credit card number is invalid!')


    print('Odd Result:', odd_result)

    print('Odd Array:', odd_array)
    print('Even Array:', even_array)
    

    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    #print(translated_card_number)

    verify_card_number(translated_card_number)

main()