# test_foundrykit.py
"""
Tests for FoundryKit module.
"""

import unittest
from foundrykit import FoundryKit

class TestFoundryKit(unittest.TestCase):
    """Test cases for FoundryKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = FoundryKit()
        self.assertIsInstance(instance, FoundryKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = FoundryKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
