# # input_str = "a a a b c a a d c d d".split()
# # letters = {}
# # for i in input_str:
# #     if i in letters.keys():
# #         print(i + "_" + str(letters[i]), end=" ")
# #         letters[i] += 1
# #     else:
# #         print(i, end=" ")
# #         letters[i] = 1
# import random
#
# # # Пользователь вводит текст(строка).
# # # Словом считается последовательность непробельных символов идущих подряд, слова разделены одним пробелом.
# # # Определите, сколько различных слов содержится в этом тексте.
# # In="She sells sea shells on the sea shore The shells that she sells are sea shells " \
# #    "I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# # print(len(set(In.upper().split())))
#
# # Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# # “Задана последовательность неотрицательных целых чисел.
# # Требуется определить значение наибольшего элемента последовательности,
# # которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# # Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание.
# # Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# #
#
# # n = int(input())
# # max_number = 0
# # while n != 0:
# #    if max_number < n:
# #        max_number = n
# #        n = int(input())
# # print(max_number)
#
#
# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# # Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# #
# n=int(input("Введите число N: "))
# m=int(input("Введите число M: "))
# arr=[random.randint(0, 20) for i in range(n)]
# print(arr)
# arr2=[random.randint(0, 20) for i in range(n)]
# print(arr2)
# res=[]
#
# print((set(arr).intersection(arr2)))
#
# # Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# # Она растет на круглой грядке, причем кусты высажены только по окружности.
# # Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# # Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# # выросло различное число ягод – на i-ом кусте выросло ai ягод.
# # В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# # Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# # Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# # собирает ягоды с этого куста и с двух соседних с ним.
# # Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# # собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
#
#
# # kusti = int(input("введите количество кустов: "))
# # berryes = list(random.randint(0, 10) for i in range(kusti))
# # result = []
# # i = 0
# # yagoda = 0
# #
# # print(berryes)
# #
# # while (i < kusti):
# #     if (i == kusti - 1):
# #         yagoda = berryes[i] + berryes[i - 1] + berryes[0]
# #     else:
# #         yagoda = berryes[i] + berryes[i - 1] + berryes[i + 1]
# #         result.append(yagoda)
# #     i += 1
# # print(max(result))
#
#
#
#
