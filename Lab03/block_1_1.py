'''Создать словарь в котором хранятся семь пар ключ-значение следующего
типа: Футболисты (str) и их результативность в 5 различных сезонах (dict)
- Вывести на экран список всех футболистов и их суммарную результативность
за 5 сезонов
- Для каждого футболиста определить сезоны с максимальной и минимальной
результативностью
- Вывести на экран всех футболистов, забивших более 30 мячей в одном из
сезонов
- Выделить всех футболистов, забивших в сезоне 2022/2023 минимум на 5 голов
больше чем в сезоне 2020 / 2021
Полученный словарь сохранить в бинарный файл data.pickle c использованием
модуля pickle. Предусмотреть возможность чтения бинарного файла и
сохранение его данных в объект словаря.'''

import pickle

footballers = {
    "Акинфеев": {
        "2018/2019": 22,
        "2020/2021": 15,
        "2022/2023": 20,
        "2023/2024": 18,
        "2024/2025": 10,
    },
    "Аршавин": {
        "2018/2019": 25,
        "2020/2021": 30,
        "2022/2023": 32,
        "2023/2024": 28,
        "2024/2025": 25,
    },
    "Кержаков": {
        "2018/2019": 18,
        "2020/2021": 10,
        "2022/2023": 5,
        "2023/2024": 12,
        "2024/2025": 1,
    },
    "Игнашевич": {
        "2018/2019": 15,
        "2020/2021": 17,
        "2022/2023": 19,
        "2023/2024": 35,
        "2024/2025": 40,
    },
    "Миранчук": {
        "2018/2019": 11,
        "2020/2021": 13,
        "2022/2023": 14,
        "2023/2024": 16,
        "2024/2025": 9,
    },
    "Карпин": {
        "2018/2019": 40,
        "2020/2021": 38,
        "2022/2023": 37,
        "2023/2024": 36,
        "2024/2025": 30,
    },
    "Аленичев": {
        "2018/2019": 20,
        "2020/2021": 22,
        "2022/2023": 27,
        "2023/2024": 30,
        "2024/2025": 24,
    },
}

print("Суммарная результативность футболистов за 5 сезонов:")
for player, seasons in footballers.items():
    total_goals = sum(seasons.values())
    print(f"{player}: {total_goals}")

print("\n")

print("Сезоны с максимальной и минимальной результативностью:")
for player, seasons in footballers.items():
    max_season = max(seasons, key=seasons.get)
    min_season = min(seasons, key=seasons.get)
    print(f"{player}: max - {max_season} ({seasons[max_season]} голов), min - {min_season} ({seasons[min_season]} голов)")

print("\n")

print("Футболисты, забившие более 30 мячей в одном из сезонов:")
for player, seasons in footballers.items():
    if any(goals > 30 for goals in seasons.values()):
        print(player)

print("\n")

print("Футболисты, у которых в сезоне 2018/2019 минимум на 5 голов больше, чем в сезоне 2020/2021:")
for player, seasons in footballers.items():
    goals_2018 = seasons.get("2018/2019", 0)
    goals_2020 = seasons.get("2020/2021", 0)
    if goals_2018 - goals_2020 >= 5:
        print(player)

print("\n")

with open("data.pickle", "wb") as f:
    pickle.dump(footballers, f)

print("Данные сохранены в файл 'data.pickle'.")

with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

print("Данные загружены из файла:")
for player, seasons in loaded_data.items():
    print(f"{player}: {seasons}")
