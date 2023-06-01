# Хакер Василий получил доступ к классному журналу и хочет заменить все
# свои минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот:
# все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
#
# Output: 1 3 3 3 1
# import random
# #
# chislo = int(input("введите количество: "))
# ocenka = list(random.randint(1, 5) for i in range(chislo))
# print(ocenka)
# maxOcenka=max(ocenka)
# for i,el in enumerate(ocenka):
#     if el == maxOcenka:
#         ocenka[i]=min(ocenka)
# print(ocenka)

# def prostoe(n):
#     if n % 2 == 0:
#         return n == 2
#     temp = 3
#     while temp * temp <= n and n % temp != 0:
#         temp += 2
#     return temp * temp > n
# print(prostoe(int(input())))

# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#
# Input:    2 -> 3 4
# Output: 4 3

# print(ocenka)
# print(*reversed(ocenka))
# print(ocenka[i] for i in range(len(ocenka)-1, -1, -1))
#
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# def sqrTemp(A,B):
#     if B==1:
#         return A
#     return A*sqrTemp(A,B-1)
#
# print(sqrTemp(2,3))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4


def sumTemp(a,b):
    if a==0:
        return b
    return sumTemp(a-1,b+1)

print(sumTemp(5,2))