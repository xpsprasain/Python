import unittest

def isVowel(a):
    if a.lower() in ('a','e','i','o','u'):
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(isVowel("a"),False)


if __name__ == '__main__':
    unittest.main()