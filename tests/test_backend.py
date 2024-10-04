import unittest
import requests
from dotenv import load_dotenv
import os

load_dotenv()


class TestBackendAPI(unittest.TestCase):

    def test_get_count(self):

        api_url = os.getenv('API_URL')

        # Call API
        response = requests.get(api_url)

        # Check if the response is 200
        self.assertEqual(response.status_code, 200, "API did not return a 200 status code.")

        # Check if the response contains the key 'count'
        json_data = response.json()
        self.assertIn('count', json_data, "'count' not found in the response JSON.")
        
        # Print the count value from the response
        print(f"Count from API: {json_data['count']}")
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
