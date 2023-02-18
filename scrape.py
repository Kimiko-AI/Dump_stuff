from bs4 import BeautifulSoup
import requests
import csv
#URL = "https://www.rpnation.com/threads/i-was-fine-until-you.482241/"
#num = 39
def scrape(URL, num, title):
    for i in range(num):
        if i ==0:
            page = requests.get(URL)
        else:
            page = requests.get(URL+"page-" + str(i+1))
        my_data = []

        soup = BeautifulSoup(page.content, 'html5lib')
        f = open(title + ".txt", "a")
        table = soup.find_all('div', attrs = {'class':'bbWrapper'})
        for x in soup.body.find_all('div', attrs = {'class':'bbWrapper'}):
            f.write(x.text)
title = input("File name ")
URL = input("URL of the page ")
num = int(input("How many page are there? "))
scrape(URL, num, title)

        