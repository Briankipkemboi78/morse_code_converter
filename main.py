morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ' ': ' '
}

# Function to convert a string to Morse code
def string_to_morse(input_string):
    input_string = input_string.upper()

    morse_code = ' '
    for char in input_string:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "
        else:
            morse_code += " "  # Use space for unknown characters
    return morse_code


input_string = input("Enter your string to be converted to morse code: ")
morse_code = string_to_morse(input_string)
print("Morse Code:", morse_code)
