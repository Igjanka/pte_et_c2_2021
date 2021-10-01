# 1. feladat
i = 1
while i <= 10:
    print(i)
    i += 1

for j in range(1,11):
    print(j)
# 2. feladat
for j in [1, 3, 5, 7, 9, 11]:
    print(j)

i = 1
while i <= 6:
    print(2 * i -1)
    i += 1

# 3. feladat

a1 = 0
a2 = 1
print(a1,a2, end=" ")
i = 0
while i < 8:
    an = a1 + a2
    a1 = a2
    a2 = an
    print(an, end=" ")
    i += 1



