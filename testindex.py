import unittest
from io import StringIO
import sys
from index import say_hello

class TestHelloWorld(unittest.TestCase):
    def test_say_hello(self):
        # Capture the output of print
        captured_output = StringIO()
        sys.stdout = captured_output  # Redirect stdout
        say_hello()  # Call the function
        sys.stdout = sys.__stdout__  # Reset stdout

        # Assert the captured output
        self.assertEqual(captured_output.getvalue().strip(), "Hello World", "The output should be 'Hello World'")

if __name__ == "__main__":
    unittest.main()
