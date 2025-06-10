#Вывести на экран синус максимального из 3 заданных чисел
import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

max_num = max(a, b, c)
sin_value = math.sin(max_num)

print(f"Синус максимального числа ({max_num}) равен {sin_value}")