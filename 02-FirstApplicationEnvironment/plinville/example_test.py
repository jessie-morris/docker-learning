import unittest

class ExampleTests(unittest.TestCase):

    def test_paul_backwards(self):
        self.assertEqual('Paul'[::-1], 'luaP')
    
    def test_uppercase(self):
        self.assertEqual('docker is cool lolz'.upper(), "DOCKER IS COOL LOLZ")

if __name__ == '__main__':
    unittest.main()
