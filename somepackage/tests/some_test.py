import unittest

from somepackage import SomeClass

class TestSomething(unittest.TestCase):
    ''' Example of a test case '''

    def test_some_method(self):
        ''' Example of a test '''

        the_answer = SomeClass.some_method()
        self.assertEqual(the_answer, 42)
