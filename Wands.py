#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

url = "harrypotter.wikia.com/wiki/Main_Page"
r = requests.get("http://" + url)
data = r.text
soup = BeautifulSoup(data)
newId = soup.find(id="gallery-3")

characters = []

for link in newId.find_all('a', attrs={"class":"image"}):
    characters.append("https://harrypotter.wikia.com" + link.get("href"))

print(characters)

def characterPage(currentCharacter):
    newr = requests.get(currentCharacter)
    newData = newr.text
    newSoup = BeautifulSoup(newData)
    name = newSoup.find('h1')
    print(name.text + '\n')
    getWand(newSoup)
    return

def getWand(newSoup):
    wands = newSoup.find(attrs={"data-source": "wand"})
    for wand in wands.find_all('a'):
        print(wand.text)
    return

for currentCharacter in characters:
    characterPage(currentCharacter)
    print('\n\n')




