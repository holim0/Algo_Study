import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# def convert(f, t):

dict = {}

list = []


def inputFun():
    while True:

        try:

            num = int(input("#: "))
            if num >= 0 and num <= len(list) - 1:

                return list[num]
                break
            else:
                print("Choose a number from the list.")
                continue
        except:
            print("That was not a number.")
            continue


def inputFun2():
    while True:
        try:
            num = int(input())
            return num
        except:
            print("That was not a number.")
            continue


url = "https://www.iban.com/currency-codes"

res = requests.get(url)

indeed_res = BeautifulSoup(res.text, "html.parser")

tbody = indeed_res.find("tbody")

tr = tbody.find_all("tr")

for t in tr:
    val = t.find_all("td")

    if val[1].text == "No universal currency":
        continue

    if val[0].text not in dict:
        dict[val[0].text] = val[2].text
    list.append(val[0].text)

list.sort()
print("Welcome to CurrencyCovert PRO 2000\n")

idx = 0

for city in list:
    print(f"# {idx} {city}")
    idx += 1

print("", end="\n")
print("Welcome are you from? Choose a country by a number.", end="\n\n")

city_From = inputFun()
print(city_From, end="\n\n")
print("Now choose another coutry.", end="\n\n")
city_To = inputFun()
print(city_To, end="\n\n")

print(f"How many {dict[city_From]} do you want to convert to {dict[city_To]}?")

money = inputFun2()

url2 = f"https://transferwise.com/gb/currency-converter/{dict[city_From]}-to-{dict[city_To]}-rate?amount={money}"

res2 = requests.get(url2)

indeed_res2 = BeautifulSoup(res2.text, "html.parser")

result = indeed_res2.select('section.m-t-2')

v = result[0].select(".text-success")

final = float(v[0].text) * money

print(format_currency(money, f"{dict[city_From]}", locale="ko_KR"), "is",
      format_currency(final, f"{dict[city_To]}", locale="ko_KR"))