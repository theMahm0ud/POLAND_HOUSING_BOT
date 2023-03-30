from bs4 import BeautifulSoup
import requests
from csv import writer
url = "https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/lodzkie?distanceRadius=0&page=1&limit=36&by=DEFAULT&direction=DESC&viewType=listing"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="css-jxeap9 e1n6ljqa2")
with open('housing.csv', 'w', encoding= 'UTF-8', newline='') as f:
 thewriter = writer(f)
 header = ['Title', 'Price']
 thewriter.writerow(header)
 for list in lists:
    title = list.find('h3', class_="css-qch36y e1n6ljqa6").text.replace('\n', '')
    price = list.find('span', class_="css-1ntk0hg ei6hyam1").text.replace('\n', '')
    info = [title, price]
    thewriter.writerow(info)
