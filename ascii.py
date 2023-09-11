A_ASCII_VALUE = ord("A")

def convert_to_ascii(character):
    my_ord = ord(character)
    print("The ASCII code of:", character, "is",my_ord)

def convert_from_ascii(ascii_value):
    my_char = chr(ascii_value)
    print("Ascii value of:", ascii_value, "is", my_char)

def alphabet_position(letter, reference):
    ascii_value = ord(letter)
    position = ascii_value - reference + 1
    print("The letter's position is: ", position, "in the alphabet")


def main():
    letter = input("Enter a character:" )
    convert_to_ascii(letter)
    convert_from_ascii(1)
    convert_from_ascii(97)
    convert_from_ascii(100)
    alphabet_position("A", A_ASCII_VALUE)
    alphabet_position("B", ord("B"))
    alphabet_position("C", ord("B"))

main()