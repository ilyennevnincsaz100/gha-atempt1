import unittest
from unittest.mock import MagicMock, patch
from bs4 import BeautifulSoup
from main.dummy_app import get_titles

class TestGetTitles(unittest.TestCase):
    def test_get_titles(self):
        # Működő mock válasz a requests modultól
        mock_response = MagicMock()
        mock_response.content = b'<html><body><h1>Title 1</h1><h2>Title 2</h2><h3>Title 3</h3></body></html>'

        # Mock requests.get függvény
        with patch('requests.get', return_value=mock_response):
            titles = get_titles('https://example.com')

        # Ellenőrzés
        self.assertEqual(titles, ['Title 1', 'Title 2', 'Title 3'])

if __name__ == '__main__':
    unittest.main()
