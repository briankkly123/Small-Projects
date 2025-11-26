import unittest
from morse import encrypt, decrypt

class TestMorseCode(unittest.TestCase):

    def test_encrypt_single_word(self):
        self.assertEqual(encrypt("HELLO"), ".... . .-.. .-.. ---")

    def test_encrypt_with_spaces(self):
        self.assertEqual(encrypt("HELLO WORLD"), ".... . .-.. .-.. ---  .-- --- .-. .-.. -..")

    def test_decrypt_single_word(self):
        self.assertEqual(decrypt(".... . .-.. .-.. ---"), "HELLO")

    def test_decrypt_with_spaces(self):
        self.assertEqual(decrypt(".... . .-.. .-.. ---  .-- --- .-. .-.. -.."), "HELLO WORLD")

    def test_encrypt_numbers(self):
        self.assertEqual(encrypt("123"), ".---- ..--- ...--")

    def test_decrypt_numbers(self):
        self.assertEqual(decrypt(".---- ..--- ...--"), "123")

    def test_round_trip(self):
        message = "THE WORLD IS VERY BRIGHT TODAY"
        encrypted = encrypt(message)
        decrypted = decrypt(encrypted)
        self.assertEqual(decrypted, message)

if __name__ == "__main__":
    unittest.main()
