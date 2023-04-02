from bs4 import BeautifulSoup  # Look for what beautifull soup is to understand
import requests  # we need this library because we will send a request to the webpage and get a response as a html text
from csv import writer
# we store the url in a variable URL
url = "https://www.olx.pl/nieruchomosci/mieszkania/wynajem/lodz/"
# we request to get the url and put it inside page, if we print page we will get Response[200] which is a HTTP response code for successful response
page = requests.get(url)
# we create an object with the class BS with two parameters one to get the content of the url and the second is to tell BS that this is an html page
soup = BeautifulSoup(page.content, 'html.parser')
# if we print soup we will get all of the source code of the url
# now we will get from soup the setion that we need
lists = soup.find_all('div', class_="css-1sw7q4x")
# Now we have stored the part that we need from the source code in lists
with open('LodzHousing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price' , 'Location/Date' , 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h6', class_="css-16v5mdi er34gjf0").text if list.find('h6', class_="css-16v5mdi er34gjf0") else '******'
        price = list.find('p', class_="css-veheph er34gjf0").text if list.find('p', class_="css-veheph er34gjf0") else '******'
        LocationAndDate = list.find('p', class_="css-10b0gli er34gjf0").text if list.find('p', class_="css-10b0gli er34gjf0") else '******'
        area = list.find('div', class_="css-1kfqt7f").text if list.find('div', class_="css-1kfqt7f") else '******'
        info = [title, LocationAndDate, price, area]
        thewriter.writerow(info)
