# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]


# a = [15, 16, 2, 3, 1, 7, 5, 4, 10]
# def big_number(a):
#     lst = []
#     for i in range(len(a) - 1):
#         n = a[i]
#         i += 1
#         m = a[i]
#         if m > n:
#             lst.append(m)
#     return lst
# print(a)       
# print(big_number(lst))



a = [15, 16, 2, 3, 1, 7, 5, 4, 10]
lst = [a[i+1] for i in range (len(a) - 1) if a[i] < a[i + 1]]
print(a)
print(lst)