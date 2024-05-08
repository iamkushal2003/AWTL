import requests
from bs4 import BeautifulSoup


# Define the URL of the website
url = 'https://www.w3schools.com/html/'


# Send a HTTP request to the specified URL and retrieve the HTML content
response = requests.get(url)
web_content = response.text


# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(web_content, 'html.parser')
print(soup.prettify())
