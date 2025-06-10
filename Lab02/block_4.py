#1. Дан одномерный массив из 10 целых чисел. Найти максимальный
#элемент и сравнить с ним остальные элементы. Вывести количество меньших
#максимального и больших максимального элемента.

numbers = [5, 7, 3, 9, 2, 9, 1, 6, 9, 4]

max_num = max(numbers)

less_than_max = 0
greater_than_max = 0

for num in numbers:
    if num < max_num:
        less_than_max += 1
    elif num > max_num:
        greater_than_max += 1

print(f"Массив: {numbers}")
print(f"Максимальный элемент: {max_num}")
print(f"Количество элементов меньше максимального: {less_than_max}")
print(f"Количество элементов больше максимального: {greater_than_max}")


#2. Одномерный массив из 10-и целых чисел заполнить с клавиатуры,
#определить сумму тех чисел, которые >5.

numbers = list(map(int, input("Введите 10 целых чисел через пробел: ").split()))

if len(numbers) != 10:
    print("Ошибка: нужно ввести ровно 10 чисел.")
else:
    total = 0
    for num in numbers:
        if num > 5:
            total += num

    print(f"Сумма чисел больше 5: {total}")
