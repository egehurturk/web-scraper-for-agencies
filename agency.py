# ---Agency Scraper---
# Python 3.7
# Author: Ege Hurturk, Cem Hurturk

import requests
from bs4 import BeautifulSoup
import openpyxl
import pyperclip
import csv
import os



allData = []

# To change the page number that you want to scrape, change the range function below. ex: range(0,3)--> will get the first 3 pages.

for pagenumber in range(0,20):

    res = requests.get('https://clutch.co/agencies/digital?page=' + str(pagenumber))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('li.provider-row')


    for i in range(len(elems)):
        row = str(elems[i])

        soup2 = BeautifulSoup(row, 'html.parser')
        try:
            companyName = soup2.select('h3.company-name > a')[0].text.strip()
        except:
            companyName = None

        websiteURL = soup2.select('li.website-link.website-link-a > a')[0]['href']

        if (companyName != None):
            allData.append(companyName.replace(",", " ") + ',' + websiteURL)

        final = []
        with open('text.csv', 'w', newline='') as f:
            a = csv.writer(f, delimiter=',')
            for index in range(len(allData)):
                final.append(",".join([allData[index]]))
                a.writerows(final)

finalresult = ''.join(final)
# pyperclip.copy(finalresult)



def main():
    filename = "agencies.csv"
    header = ("Agency", "Company Name")
    writer(header, final, filename)

def writer(header, data, filename):
  with open (filename, "w", newline = "\n") as csvfile:
    infos = csv.writer(csvfile)
    infos.writerow(header)
    for x in data:
        infos.writerow(x.split(","))


# Works ONLY when the code is executed from the local:

if __name__ == "__main__":
     main()
