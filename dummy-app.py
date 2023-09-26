import requests
from bs4 import BeautifulSoup

def get_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all(['h1', 'h2', 'h3'])

    return [title.text for title in titles]

url = 'https://example.com'

titles = get_titles(url)

print("Titles on the webpage:")
for title in titles:
    print(title)