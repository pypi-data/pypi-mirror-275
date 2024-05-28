import unittest
from unittest.mock import patch
from qiskit_pqcee_provider.provider import Provider

class TestProvider(unittest.TestCase):
    @patch.dict('os.environ', {'ALCHEMY_API_KEY': 'test_key'})
    def test_alchemy_api_key(self):
        provider = Provider()
        self.assertEqual(provider.alchemy_api_key, 'test_key')

if __name__ == '__main__':
    unittest.main()