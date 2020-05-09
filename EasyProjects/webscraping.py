from tkinter import messagebox as mb

import requests
from bs4 import BeautifulSoup


class WebScraping:
    # url="https://classnotes.org.in/class-11/"
    # url = 'https://www.worldometers.info/coronavirus/'
    def __init__(self):
        url = "https://www.mohfw.gov.in/"
        print("Corona Virus Data in India, extracted from official government website")
        result = requests.get(url)
        src = result.content
        soup = BeautifulSoup(src, "html.parser")
        # India Details
        b = soup.find_all("span")
        details = []
        for link in b:
            if "Active Cases" in link.text:
                details.append("Active Cases in India Till Now " + link.parent.contents[3].text)
            if "Cured / Discharged " in link.text:
                details.append("Cured Cases in India Till Now " + link.parent.contents[3].text)
            if "Deaths" in link.text:
                details.append("Deaths in India Till Now " + link.parent.contents[3].text)
        # Odisha Details
        b = soup.find_all("td")
        for link in b:
            if "Odisha" in link.text:
                details.append("Active cases in Orissa till now: " + link.parent.contents[5].text)
                details.append("Cured in Orissa till now: " + link.parent.contents[7].text)
                details.append("Deaths in Orissa till now: " + link.parent.contents[9].text)
        detailstr = ""
        # Tkinter Message Boc
        for x in range(len(details)):
            detailstr = details[x] + "\n"
            mb.showinfo(title='Corona Virus Detail Report', message=detailstr)



