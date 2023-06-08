# values = [1, 23, 42, "asdfg"]
#
#
# transformed_values = list(map(lambda x:x, values))
#
# print(transformed_values)
# if values == transformed_values:
#  print("ok")
# else:
#  print("fail")

string = "пара-ра-рам рам-пам-папам па-ра-па-дам "
print('Парам пам-пам' if 1 not in list(map(lambda x: x.count('а')%2,string.split())) else "Пам парам")

def print_operation_table(operation, num_rows=6, num_columns=6):
 for row in range(1, num_rows + 1):
  for column in range(1, num_columns + 1):
   print(operation(row, column), end='\t')
  print()
print_operation_table(lambda x, y: x * y)




