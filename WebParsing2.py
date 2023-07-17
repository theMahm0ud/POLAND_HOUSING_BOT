from bs4 import BeautifulSoup
import requests  
from csv import writer

url = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/lodz/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

lists = soup.find_all('div', class_="css-1sw7q4x")

with open('LodzHousingWlink.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price', 'Location/Date', 'Area', 'Link']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h6', class_="css-16v5mdi er34gjf0").text if list.find(
            'h6', class_="css-16v5mdi er34gjf0") else '******'
        price = list.find('p', class_="css-veheph er34gjf0").text if list.find(
            'p', class_="css-veheph er34gjf0") else '******'
        LocationAndDate = list.find('p', class_="css-10b0gli er34gjf0").text if list.find(
            'p', class_="css-10b0gli er34gjf0") else '******'
        area = list.find('div', class_="css-1kfqt7f").text if list.find('div',
                                                                        class_="css-1kfqt7f") else '******'
        link = list.find('a')['href'] if list.find('a') else '******'
        info = [title, LocationAndDate, price, area, link]
        thewriter.writerow(info)