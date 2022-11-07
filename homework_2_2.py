#Задание 4-1
import math
print("Задание 4-1")
print("Введите 1-e значение    ")
a = int(input())
print("Введите 2-e значение    ")
b = int(input())
print("Введите 3-e значение    ")
c = int(input())
if (a < b) or (a < c) :
    print("Наименьшее значение-  ", a)
elif (b < c) or (a < c) :
    print("Наименьшее значение-  ", b)
else:
    print("Наименьшее значение-  ", c)

#Задание 4-2
print("Задание 4-2")
print("Введите 1-e значение    ")
d = int(input())
print("Введите 2-e значение    ")
e = int(input())
print("Введите 3-e значение    ")
q = int(input())
if (d == e) and (e == q):
    s = 3
elif (d == e) or (d == q):
    s = 2
else:
    s = 0
print("Надено ", s, "совпадений.")

#Задание 4-3
print("Задание 4-3")
print("Введите номер столбца,от 1 до 8:")
move_a1 = int(input())
print("Введите номер строки, от 1 до 8")
move_b1 = int(input())
print("Введите номер столбца, от 1 до 8")
move_a2 = int(input())
print("Введите номер строки, от 1 до 8")
move_b2 = int(input())
print("Введите номер столбца, от 1 до 8")
if move_a1 == move_a2 or move_b1 == move_b2:
    print("Да")
else:
    print("Нет")
