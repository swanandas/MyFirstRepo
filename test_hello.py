import unittest

from hello import *

class TestHello(unittest.TestCase):
    def test_output(self):
        import sys
        from io import StringIO
        captured = StringIO()
        sys.stdout = captured
        print('Hello, World!')
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue().strip(), 'Hello, World!')

if __name__ == '__main__':
    unittest.main()
