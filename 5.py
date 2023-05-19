# Задана рекуррентная функция. Область определения функции – натуральные числа.
# Написать программу сравнительного вычисления данной функции рекурсивно и итерационно.
# Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме.
# 15.F(0) = 1, F(1) = 1, F(n) = 2*F(n–1) + F(n-2), при n > 1
import time
import matplotlib.pyplot as plt

a = []
b = []
x = []


def rec(w):
    if w == 0:
        return 1
    if w == 1:
        return 1
    if w > 1:
        return 2 * rec(w - 1) + rec(w - 2)


def iter(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        f = [1] * 4
        for i in range(2, n + 1):
            f[3] = 2 * f[2] + f[1]
            f[0], f[1], f[2] = f[1], f[2], f[3]
        return f[3]


print("Примечание: рекомендуется вводить n<35. При бо́льших значениях вычисление рекурсии занимает много времени")
print("Введите число для количества вычислений:", end='')
m = int(input())
if 30 < m < 50:
    print("Значение есть, идёт подсчёт, пожалуйста, подождите")
elif m >= 50:
    print('Ошибка, программа будет вычисляться слишком долго, пожалуйста, введите значение меньше 50')
    exit()
print("Значения рекурсии и итерации от 1 до n:")
for i in range(1, m + 1):
    print(rec(i), iter(i))
    x.append(i)
print('')
print('№' + '        ' + 'Рекурсивно' + '           ' + 'Итеративно')
for n in range(1, m + 1):  # заполнение списков данными
    start = time.perf_counter()
    rec(n)
    end = time.perf_counter()
    print(str(n) + ' | ' + str(end - start) + " | ", end='')
    a.append(end - start)
    start = time.perf_counter()
    iter(n)
    end = time.perf_counter()
    print(str(end - start))
    b.append(end - start)
y1 = a
y2 = b
plt.xlabel('Число, которое подаётся')
plt.ylabel('Время поиска в миллисекундах')
plt.plot(x, y1, label='Рекурсивно')
plt.plot(x, y2, label='Итеративно')
plt.legend()
plt.show()
