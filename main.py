from morse.converter import encrypt, decrypt

def main():
    """
    Main function that handles user interaction for converting
    text to Morse code and vice versa.
    """
    choice = input("Type 'T' for Text to Morse Code or 'M' for Morse Code to Text: ").upper()
    
    if choice == 'T':
        message = input("Enter your message: ").upper()
        try:
            result = encrypt(message)
            print("Morse Code:", result)
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == 'M':
        message = input("Enter your Morse Code: ")
        try:
            result = decrypt(message)
            print("Text:", result)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice. Please type 'T' or 'M'.")

if __name__ == "__main__":
    main()