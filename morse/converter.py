# morse/converter.py

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', 
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

INVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encrypt(message):
    """
    Convert a text message to Morse code.
    
    Args:
        message (str): The text message to be converted.
        
    Returns:
        str: The converted Morse code.
        
    Raises:
        ValueError: If the message contains characters not in the Morse code dictionary.
    """
    morse_code = []
    for letter in message:
        if letter in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[letter])
        else:
            raise ValueError(f"Character '{letter}' cannot be converted to Morse code.")
    return ' '.join(morse_code)

def decrypt(morse_code):
    """
    Convert a Morse code message to text.
    
    Args:
        morse_code (str): The Morse code message to be converted.
        
    Returns:
        str: The converted text message.
        
    Raises:
        ValueError: If the Morse code contains invalid sequences.
    """
    message = []
    for code in morse_code.split(' '):
        if code in INVERSE_MORSE_CODE_DICT:
            message.append(INVERSE_MORSE_CODE_DICT[code])
        else:
            raise ValueError(f"Morse code '{code}' is invalid.")
    return ''.join(message)