import unittest
from apiverve_timezonelookup.apiClient import TimezonelookupAPIClient
from unittest.mock import patch

class TestTimezonelookupAPIClient(unittest.TestCase):

    def setUp(self):
        self.api_key = 'test_api_key'
        self.client = TimezonelookupAPIClient(self.api_key)

    @patch('apiverve_timezonelookup.apiClient.requests.get')
    def test_make_request_success(self, mock_get):
        # Assuming there's an endpoint 'test_endpoint' for testing purposes
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'test': 'test'}
        response = self.client.get('test_endpoint')
        self.assertIsInstance(response, dict)

    @patch('apiverve_timezonelookup.apiClient.requests.get')
    def test_make_request_failure(self, mock_get):
        # Assuming there's an endpoint 'test_endpoint' for testing purposes
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception):
            self.client.get('test_endpoint')

if __name__ == '__main__':
    unittest.main()
