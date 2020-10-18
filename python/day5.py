import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

res = requests.get(url)

indeed_res = BeautifulSoup(res.text, "html.parser")

tbody = indeed_res.find("tbody")

tr = tbody.find_all("tr")

dict = {}

list = []

for t in tr:
    val = t.find_all("td")

    if val[1].text == "No universal currency":
        continue

    dict[val[0].text] = val[2].text
    list.append(val[0].text)

list.sort()
print("Hello! Please choose select a country by number:\n")

idx = 0

for city in list:
    print(f"# {idx} {city}")
    idx += 1

while True:

    try:
        num = int(input("#: "))

        if num >= 0 and num <= len(list) - 1:
            print(f"You choose {list[num]}")
            print(f"The currency code is {dict[list[num]]}")
            break
        else:
            print("Choose a number from the list.")
            continue
    except:
        print("That was not a number.")
        continue










