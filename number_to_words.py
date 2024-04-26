

def number_to_words(number):
    # Dictionary mapping numbers to their word representations
    number_words = {
        0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 
        5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 
        10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 
        14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 
        18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 
        40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 
        80: 'Eighty', 90: 'Ninety'
    }

    # Special cases for numbers less than 20
    if number <= 20:
        return number_words[number]

    # Convert tens and ones digits separately
    tens_digit = number // 10 * 10
    ones_digit = number % 10

    # Construct word representation for numbers greater than 20
    if ones_digit == 0:
        return number_words[tens_digit]
    else:
        return number_words[tens_digit] + '-' + number_words[ones_digit]

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    print("Word representation:", number_to_words(user_input))
