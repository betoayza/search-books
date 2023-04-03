import requests
from bs4 import BeautifulSoup

book = input("\nSearch book: ")

URL = f"https://www.google.com/search?tbm=bks&q={book}"
response = requests.get(URL)
response_code = response.status_code
html_text = response.text
# print([response_code, html_text])


if response_code == 200:    
    html = BeautifulSoup(html_text, "html.parser")
    entries = html.find_all('h3')  

    for i, entry in enumerate(entries):
        title = entry.find('div').getText()
        print(i+1, title)



