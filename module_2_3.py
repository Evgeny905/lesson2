my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_spisok = 0
max_spisok = len(my_list) - 1

while index_spisok < max_spisok:
    if my_list[index_spisok] > 0:
        print(my_list[index_spisok])
        break

while index_spisok < max_spisok:
    index_spisok = index_spisok + 1
    if my_list[index_spisok] > 0:
        print(my_list[index_spisok])
    elif my_list[index_spisok] < 0:
        break