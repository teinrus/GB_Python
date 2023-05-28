# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
# import random
# N=int(input("Введите число N: "))
# X=int(input("Введите число X: "))
# arr=[random.randint(0, 10) for i in range(N)]
# print(arr)
# print(arr.count(X))

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N
# целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
# print(max(el for el in arr if el >= X))

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков; J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12




N=input("Введите слово : ").upper()

dic={1:('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т','A', 'E', 'I', 'O','U','L', 'N', 'S', 'T', 'R'),2:('Д', 'К', 'Л', 'М', 'П', 'У','D', 'G'),
3:('Б', 'Г', 'Ё', 'Ь', 'Я','B', 'C', 'M', 'P'), 4:('Й', 'Ы','F', 'H', 'V', 'W', 'Y'),5:('Ж', 'З', 'Х', 'Ц', 'Ч','K')
     ,8:('Ш', 'Э', 'Ю','J', 'X'),10:('Ф','Щ', 'Ъ','Q', 'Z')}
result=0

for bookva in N:
    for k,el in dic.items():
        if bookva in el:
            result+=k
print(result)


