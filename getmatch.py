import requests
from bs4 import BeautifulSoup
from datetime import date
from time import gmtime, strftime

day = date.today()
d = day.strftime('%Y%m%d')
dayd = day.strftime('')
def getmatch():
    source = requests.get('https://www.espn.com/soccer/fixtures/_/date/'+ d +'/league/bra.1').text
    soup = BeautifulSoup(source,'lxml')

    for match in soup.find_all('tr', class_='even'):
       print(match.text, "\n")


    for match2 in soup.find_all('tr', class_='odd'):
       print(match2.text, "\n")

print("\nThe Matches that will occur in the Brazilian A League for "+ strftime("%a, %d %B of %Y")+ ", are: \n")
getmatch()
