'''Используя библиотеки requests и beautifulsoup4 произвести скрейпинг страниц
сайта https://worldathletics.org.
- Перейти в раздел https://worldathletics.org/records/toplists
- Проанализировать закономерности изменения адресов страниц при смене года,
пола спортсмена и дисциплины
- Проанализировать код страницы (найти теги, отвечающие за представление
информации о результате, имени спортсмена, стране и дате соревнования)
Получить информацию о лучших результатах (топ-1) у мужчин и женщин в
дисциплинах 800м, 1500м, 5000м, 10000м за 2001-2024 годы. Данные (год, имя
спортсмена, страна, время, дата соревнования) сохранить в файле top_results.csv'''

import requests, csv, random
from bs4 import BeautifulSoup

#women
#800 - 10229512
#1500 - 10229513
#5000 - 10229514
#10000 - 10229521

#men
#800 - 10229501
#1500 - 10229502
#5000 - 10229609
#10000 - 10229610

years = 24
genders = {
    "women": {
        "800-metres": 10229512,
        "1500-metres": 10229513,
        "5000-metres": 10229514,
        "10000-metres": 10229521
    },
    "men": {
        "800-metres": 10229501,
        "1500-metres": 10229502,
        "5000-metres": 10229609,
        "10000-metres": 10229610
    }
}

records = []

for year in range(2025 - years, 2025):
    for gender in genders:
        for discipline in genders[gender]:
            print(discipline)

            eventId = genders[gender][discipline]
            response = requests.get(f"https://worldathletics.org/records/toplists/sprints/{discipline}/all/{gender}/senior/{year}?regionType=world&timing=electronic&page=1&bestResultsOnly=true&maxResultsByCountry=all&eventId={eventId}&ageCategory=senior", verify=False)

            print(f"https://worldathletics.org/records/toplists/sprints/{discipline}/all/{gender}/senior/{year}?regionType=world&timing=electronic&page=1&bestResultsOnly=true&maxResultsByCountry=all&eventId={eventId}&ageCategory=senior")
            soup = BeautifulSoup(response.text, "html.parser")

            record = {}
            record["name"] = soup.select(".records-table tr:first-of-type [data-th='Competitor'] a")[0].text.strip()
            record["country"] = soup.select(".records-table tr:first-of-type [data-th='Nat']")[0].text.strip()
            record["time"] = soup.select(".records-table tr:first-of-type [data-th='Mark']")[0].text.strip()
            record["date"] = soup.select(".records-table tr:first-of-type [data-th='Date']")[0].text.strip()
            record["year"] = year
            record["discipline"] = discipline
            record["gender"] = gender
            print(soup.select(".records-table tr:first-of-type [data-th='Nat']")[0].text.strip())

            records.append(record)

print(records)
with open("records.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["year", "name", "country", "time", "date", "discipline", "gender"])
    writer.writeheader()
    writer.writerows(records)



