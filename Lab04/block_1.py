'''Используя библиотеку requests и сторонний API получить данные о западно-
африканских странах, с численностью населения более 10 миллионов человек.
(справка для получения адреса api https://restcountries.com/#endpoints-subregions)
-Сохранить данные об имени стран, столицах, площади и численности населения,
списке соседей в файл results.json (https://restcountries.com/#endpoints-filter-response
для справки).
-Для каждой страны вычислить количество соседей.
-Вывести в консоль топ-3 стран (имена) по числу соседей .
-.png флаги каждой из 3 стран сохранить отдельными файлами'''

import requests, json

response = requests.get('https://restcountries.com/v3.1/region/Western Africa')

countries = []

for country in response.json():
    if (country["population"] <= 10000000):
        continue

    countryObj = {}
    countryObj["name"] = country["name"]["common"]
    countryObj["capital"] = country["capital"][0]
    countryObj["area"] = country["area"]
    countryObj["population"] = country["population"]
    countryObj["borders"] = country["borders"]
    countryObj["borders_count"] = len(country["borders"])
    countryObj["flag"] = country["flags"]["png"]

    countries.append(countryObj)

print("Топ три страны по числу соседей:")
for country in sorted(countries, key=lambda country: country["borders_count"], reverse=True)[:3]:
    print(f"{country['name']}, соседи: {country['borders']}")

    response = requests.get(country["flag"])
    with open("flags/" + country["name"] + "_flag.png", "wb") as f:
        f.write(response.content)


with open("results.json", "w", encoding="utf-8") as f:
    json.dump(countries, f, ensure_ascii=False, indent=2)


