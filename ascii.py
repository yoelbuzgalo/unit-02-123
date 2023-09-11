def convert_to_ascii(character):
    my_ord = ord(character)
    print("The ASCII code of:", character, "is",my_ord)

def convert_from_ascii(ascii_value):
    my_char = chr(ascii_value)
    print("Ascii value of:", ascii_value, "is", my_char)


def main():
    letter = input("Enter a character:" )
    convert_to_ascii(letter)
    convert_from_ascii(1)
    convert_from_ascii(97)
    convert_from_ascii(100)

main()