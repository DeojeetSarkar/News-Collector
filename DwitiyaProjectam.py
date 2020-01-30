import requests
from bs4 import BeautifulSoup


source = requests.get("https://timesofindia.indiatimes.com/").text
soup = BeautifulSoup(source,'lxml')

for headline in soup.find_all(class_ = 'list9'):
    print(headline.text)
