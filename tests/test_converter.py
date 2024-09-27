import unittest
from morse.converter import encrypt, decrypt

class TestMorseCodeConverter(unittest.TestCase):

    def test_encrypt_single_word(self):
        self.assertEqual(encrypt("HELLO"), ".... . .-.. .-.. ---")

    def test_encrypt_sentence(self):
        self.assertEqual(encrypt("HELLO WORLD"), ".... . .-.. .-.. --- / .-- --- .-. .-.. -..")

    def test_encrypt_with_numbers(self):
        self.assertEqual(encrypt("HELLO 123"), ".... . .-.. .-.. --- / .---- ..--- ...--")

    def test_encrypt_with_punctuation(self):
        self.assertEqual(encrypt("HELLO, WORLD!"), ".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--")

    def test_decrypt_single_word(self):
        self.assertEqual(decrypt(".... . .-.. .-.. ---"), "HELLO")

    def test_decrypt_sentence(self):
        self.assertEqual(decrypt(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")

    def test_decrypt_with_numbers(self):
        self.assertEqual(decrypt(".... . .-.. .-.. --- / .---- ..--- ...--"), "HELLO 123")

    def test_decrypt_with_punctuation(self):
        self.assertEqual(decrypt(".... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--"), "HELLO, WORLD!")

    def test_encrypt_unknown_character(self):
        self.assertEqual(encrypt("HELLO$"), ".... . .-.. .-.. --- ?")

    def test_decrypt_unknown_morse_code(self):
        self.assertEqual(decrypt(".... . .-.. .-.. --- ?"), "HELLO?")

if __name__ == "__main__":
    unittest.main()