# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# def find (a, n):
#     a = 20
#     n = int(input("Введите число: "))
#     list = [i for i in range(a, n) if i % 20 == 0 or i % 21 == 0]

# print(find(list))

n = int(input("Введите число: "))
list = [i for i in range(20, n + 1) if i % 20 == 0 or i % 21 == 0]

print("кратные числа 20 или 21 в диапазоне от 20 до вашего числа будет: ", list)