"""Test example_module."""
import unittest

from examplepkglearnpython import example_module


class TestExampleModule(unittest.TestCase):
    """Test example_module."""
    
    def test_hello(self):
        """Test hello."""
        expected = 'Hello World!'
        greeting = example_module.hello()
        self.assertEqual(greeting, expected)

