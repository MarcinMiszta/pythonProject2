import sys
# a = 56
# print(a)
# print(type(a))
# b = 5.5
# print(b)
# print(type(b))
# zmienna_tekstowa = 'wizualizacja danych'
# print(zmienna_tekstowa)
# print(type(zmienna_tekstowa))

# a = 6
# b = 3
#
# c = a + b
# print(c)
# d = a - b
# print(d)
# e = 4
# f = b // a
# print(f)
# f = a // b
# print(f)
#
# g = a ** 2
# print(g)
# h = pow(a, 2)
# print(h)
# i = 6 ** (1/2)
# j = pow(6, 1/2)
# print(i)
# print(j)
# k = 'wizualizacja danych'
# l = ' grupa 1'
# m = 1
# print(k + l + str(m))
# print('liczba a jest rowna {:.2f}, liczba b jest rowna {:.2f}'
#       .format(a, b))

# a = input('wprowadz liczbe: ')
# print(a)
# print(type(a))
# print(a*5)
# print(type(a))
#
# sys.stdout.write('Wprowadz liczbe ')
# b = sys.stdin.readline()
# print(b)
# print(type(b))
lista = [6, 6.6, 34, 'a', 'b', [2, 3, 4], 'ab']
print(lista)
lista.append(67)
print(lista)
lista.insert(2,'c')
print(lista)
lista.extend([20, 21, 22])
print(lista)
lista.pop()
print(lista)
lista.remove([2, 3, 4])
print(lista)
del lista[1]
print(lista)
del lista
