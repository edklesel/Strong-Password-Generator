import unittest
from generate_password import generate_password
import pyperclip

def retain_clipboard(function):
    def wrapper(self, *args, **kwargs):
        clipboard = pyperclip.paste()
        function()
        pyperclip.copy(clipboard)
    return wrapper

class TestStrength(unittest.TestCase):

    def test_length(self):
        password = generate_password()
        self.assertGreaterEqual(len(password),8)

    def test_minlength(self):
        password = generate_password(length=5)
        self.assertIn('ERROR', password) 

    def test_number(self):
        password = generate_password()
        self.assertRegex(password, '[0123456789]')

    def test_symbol(self):
        password = generate_password()
        self.assertRegex(password, '[\!\"\£\$\%\^\&\*\(\)\-\_\=\+\[\]\{\}\@\~\#\,\.\<\>\/\?\|]')

    def test_upper(self):
        password = generate_password()
        self.assertRegex(password, '[ABCDEFGHIJKLMNOPQRSTUVWXYZ]')


class TestClipboard(unittest.TestCase):

    # @retain_clipboard
    def test_copy(self):
        pyperclip.copy('blank')
        password = generate_password(clipboard=True)
        self.assertEqual(password, pyperclip.paste())

    # @retain_clipboard
    def test_nocopy(self):
        pyperclip.copy('blank')
        password = generate_password(clipboard=False)
        self.assertNotEqual(password, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()