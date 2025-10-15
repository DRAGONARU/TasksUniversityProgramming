# task 1

'''
temp_celsus = float(input())
temp_fahrenheit = (temp_celsus * 9/5) + 32
temp_kelvin = temp_celsus + 273.15
print(f"Температура в цельсиях {temp_celsus} градуса = Температура в фаренгейтах: {round(temp_fahrenheit, 2)} градуса\n")
print(f"Температура в цельсиях {temp_celsus} градуса = Температура в кельвинах: {round(temp_kelvin, 2)} градуса\n")
'''

#task 2

'''
a = int(input())
if a % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
if a > 0:
    print("Положительное")
elif a < 0:
    print("Отрицательное")
else:
    print("Ноль")
if 10 <= a <= 50:
    print("Принадлежит диапозону [10, 50]")
else:
    print("Не принадлежит диапозону [10, 50]")
'''

#task 3
'''
from random import randint
from random import shuffle
spetz = '!@#$%^&*'
pas = ''
pas += chr(randint(65, 90))
pas += chr(randint(65, 90))
pas += chr(randint(65, 90))
pas += chr(randint(48, 57))
pas += chr(randint(48, 57))
pas += chr(randint(48, 57))
pas += spetz[randint(0, 7)]
pas += spetz[randint(0, 7)]
pas = list(pas)
shuffle(pas)
shuffled_pas = ''.join(pas)
print(shuffled_pas)
'''
#task 4
'''
a = input().lower()
list_of_quantity = [0] * 128
for i in a:
    list_of_quantity[ord(i)] += 1
mx1 = 0
mxi1 = 0
mx2 = 0
mxi2 = 0
mxi3 = 0
mx3 = 0
for i in range(128):
    if list_of_quantity[i] > mx1:
        mx3 = mx2
        mxi3 = mxi2
        mx2 = mx1
        mxi2 = mxi1
        mx1 = list_of_quantity[i]
        mxi1 = i
    if list_of_quantity[i] > mx2 and i != mxi1 and i != mxi3:
        mx3 = mx2
        mxi3 = mxi2
        mx2 = list_of_quantity[i]
        mxi2 = i
    if list_of_quantity[i] > mx3 and i != mxi1 and i != mxi2:
        mx3 = list_of_quantity[i]
        mxi3 = i
print(str(chr(mxi1)), str(chr(mxi2)), str(chr(mxi3)))
print(mx1, mx2, mx3)
'''
#task 5
'''
n = int(input())

a = [i for i in range(2, n + 1)]
for i in range(len(a)):
    err = []
    for j in range(i + 1, len(a)):
        if a[j] % a[i] == 0:
            err.append(a[j])
    for k in err:
        a.remove(k)
print(a)
'''
#task 5 optimised
'''
N = int(input())
lp = [0] * (N + 1)
pr = []

for i in range(2, N + 1):
    if lp[i] == 0:
        lp[i] = i
        pr.append(i)
    for j in range(len(pr)):
        if pr[j] > lp[i] or i * pr[j] > N:
            break
        lp[i * pr[j]] = pr[j]
print(pr)
'''
#task 6
'''
def sumnomera(n):
    co = 0
    for i in range(n):
        co += 10 ** i * (i + 1) * 9
    return co
N = int(input())
cifra_count = 1
while sumnomera(cifra_count) < N:
    cifra_count += 1
offset = N - sumnomera(cifra_count - 1) - 1
index = offset // cifra_count
number = 10 ** (cifra_count - 1) + index
digit = offset % cifra_count
print(str(number)[digit])
'''
