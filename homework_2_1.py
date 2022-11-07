#Задание 3.1
print ("Задание 3-1")
import math

a= input(" Введите значение 1-    ")
b = input(" Введите значение 2-    ")
if (a < b):
    print("Наименьшее значение-  ", a)
else:
    print ("Наименьшее значение-  ", b)
# Задание 3.2
print ("Задание 3-2")
c=int(input(" Введите значение -    "))
if c > 0:
    print("Значение sign(x)-  ", 1)
elif c < 0:
    print("Значение sign(x)-  ", -1)
else:
    print ("Значение sign(x)-  ", 0)

#Задание 3.3
print ("Задание 3-3")
print ("Введите номер столбца,от 1 до 8:")
move_a1= int(input())
print ("Введите номер строки, от 1 до 8")
move_b1= int(input())
print ("Введите номер столбца, от 1 до 8")
move_a2= int(input())
print ("Введите номер строки, от 1 до 8")
move_b2= int(input())
print ("Введите номер столбца, от 1 до 8")
if ((move_a1 %2==0 and move_a2 %2==0) and (move_b1 %2==0 and move_b2 %2==0)) :
    print("Да, клетки доски имеют одинаковый цвет.")
elif ((move_a1 %2!=0 and move_a2 %2!=0) and (move_b1 %2!=0 and move_b2 %2!=0)) :
    print("Да, клетки доски имеют одинаковый цвет.")
else:
    print("Нет, клетки доски имеют разные цвета.")
