# test_bcrypthash.py
"""
Tests for BcryptHash module.
"""

import unittest
from bcrypthash import BcryptHash

class TestBcryptHash(unittest.TestCase):
    """Test cases for BcryptHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BcryptHash()
        self.assertIsInstance(instance, BcryptHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BcryptHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
