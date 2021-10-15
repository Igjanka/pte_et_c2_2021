#1

km_m= 1000
h_s = 3600
try:
    speed_km_h = float(input("Kérem adja meg a sebbességet: "))
    speed_m_s = speed_km_h * 1000 / 3600
    print(f" A {speed_km_h} km/h sebesség az {speed_m_s} m/s")
except:
    print("Sajnálom, de nem tudom átváltani.")

#2

import random
random_numbers = []
for number in range(10):
    random_numbers.append(random.randint(1, 100))
even_numbers = []
odd_numbers = []
for i in range(len(random_numbers)):
    if random_numbers[i] % 2 == 0:
        even_numbers.append(random_numbers[i])
    else:
        odd_numbers.append((random_numbers[i]))

print("A generált számsor:", random_numbers)
print("Ebből a párosak:", even_numbers)
print("Ebből a páratlanok:", odd_numbers)

#3










#4
a = []
while 1:
    b = input(f"Kérek egy karaktert: ")
    if(len(b)>0):
        a.append(b)
        print(a)
    else:
        break

#5

import random
numbers = []
for i in range(20):
    numbers.append(random.randint(1,100))

min_value = numbers[0]
max_value = numbers[0]
for number in numbers:
    if min_value > number:
        min_value = number
    if max_value < number:
        max_value = number

print(numbers)
print(min_value)
print(max_value)

#6

name = input("Kérem adja meg a nevét: ")
gender = input()

#7
try:
    a = input("A háromszög a oldalának hossza: ")
    b = input("A háromszög b oldalának hossza: ")
    c = input("A háromszög c oldalának hossza: ")
    if a+b >c and b+c >a and a+c >b:
         print("A háromszög létezik.")
except:
    print("Egy szám kell")
