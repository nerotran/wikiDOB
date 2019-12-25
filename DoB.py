from bs4 import BeautifulSoup
import requests
import csv

readName = "Characters.wiki"
writeName = "DOB.csv"

with open(writeName, "w", newline = "") as fw:
    fieldnames = ["Name", "DoB"]
    csv_writer = csv.DictWriter(fw, fieldnames=fieldnames)
    csv_writer.writeheader()
    with open(readName, "r") as fr:
        for line in fr.readlines():
            url = "https://en.wikipedia.org/wiki/"
            name = line.strip("\n")
            url += name
            source = requests.get(url).text
            soup = BeautifulSoup(source, "lxml")
            dob = soup.find("span", class_="bday").text
            csv_writer.writerow({"Name": name, "DoB": dob})












