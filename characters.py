def add_chars(char_1, char_2):
    '''
    This function takes in two character parameters and will print out the added sum of the ascii values and the new ascii character of it
    '''
    add_ascii_num = ord(char_1) + ord(char_2) # Converts both characters from parameter to ascii value and adds them both
    print("The added sum of ascii values of the characters are: ",add_ascii_num, " and the new ASCII character of it is: ", chr(add_ascii_num)) # Prints to the terminal the results

def subtract_chars(char_1, char_2):
    '''
    This function takes in two character parameters and will print out the subtracted sum of the ascii values and the new ascii character of it
    '''
    subtract_ascii_num = ord(char_1) - ord(char_2) # Converts both characters from parameter to ascii value and subtracts them both
    print("The subtracted sum of ascii values of the characters are: ",subtract_ascii_num, " and the new ASCII character of it is: ", chr(subtract_ascii_num)) # Prints to the terminal the results


def main():
    letter_1 = input("Enter first letter: ")
    letter_2 = input("Enter second letter: ")
    add_chars(letter_1,letter_2)
    subtract_chars(letter_1, letter_2)
main()


'''
Few things happened:
1. Odd characters, this happens when I enter "B" then "A", some emojis and different language letter were printed to the console. This happens because python has unicode as well and not just ASCII.
2. If I try to enter "A" then "B", it will be an error out of range because it's value becomes a minus (A minus B) while B is greater than A, there is no corresponding letter that matches within the range.
3. If I try to enter more than 1 character per input, it will say "ord() expected a character, but a string of length 3 found" which means that it can only convert 1 letter and not 3 letters.
'''