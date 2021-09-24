import random


number = int(input("Adj meg egy számot: "))
if number <= 10:
    print("Ez a szám kisebb vagy egyenló 10-el.")
else:
    print("Ez a szám nem kisebb vagy egyenlő 10-el.")

#fel_1

if number > 100:
    print("Ez a szám nagyobb, mint 100.")
else:
    print("Ez a szám nem nagyobb, mint 100.")

#fel_2

if number % 2 > 0:
    print("A szám páratlan")
else:
    print("A szám páros")

#fel_3

number2 = 20
if number % number2 == 0:
    print("A", number2,"osztója a", number)
else:
    if number2 % number == 0:
        print("A", number2," osztója a", number)
    else:
        print("Egyik sem osztója a másiknak")

#fel_4


str = "alma"
if str[0] == str[-1]:
    print("A szöveg első betűje megegyezik az utolsóval.")
else:
    print("A szöveg első betűje nem egyezik meg az utolsóval.")

#fel_5

if number > 0:
    print("pozitív")
elif number < 0:
    print("negatv")
else:
    print("nulla")

    #fel_6

if str[0].isupper():
    print("Nagybetűvel kezdődik")
else:
    print("Nem nagybetűvel keződik")

str2 = "almafa"
str3 = "almaszár"

if str3[0:5] == str2[0:5]:
    print("Az első 5 karakter azonos")
else:
    print("Az első 5 karakter azonos")
    
#pl_1

if number >= 3 and number < 17:
    print("Beleesik  a szám a [3. 17) intervallumba")
else:
    print("Nem esik bele a szám a [3. 17) intervallumba")

#pl_2

a,b,c = random.randint(1,100),random.randint(1,100),random.randint(1,100)

if a + b > c and b + c > a:
    print(" Lehet háromszöget szerkeszteni")
else:
    print("Nem lehet háromszöget szerkeszteni")

#pl_3

if a > b and a > c:
    print("a a legnagyobb")
if b > a and b > c:
    print("b a legnagyobb")
else:
    print("c a legnagyobb")

if a < b and a < c:
    print("a a legkisebb")
if b < a and b < c:
    print("b a legkisebb")
if c < a and c < b:
    print("c a legkisebb")

#pl_4

str5 = "fagyi"
mag_h = ("a","e","i","o","u")
if str5 [0] == mag_h:
    print("Magánhangzó")
else:
    print("Nem magánhangzó")

#other_option
character = "a"
numbers = "123456789"
irasjelek = ",.?:;"
maganhangzok = "aeuioéáőúűóüöíAEUIOÖÜÓŐÚŰÁÉÍ"
if maganhangzok.find(character) >=0:
    print("magánhangzó")
elif numbers.find(character) >=0:
    print("magánhangzó")
elif irasjelek.find(character) >=0:
    print("magánhangzó")

#pl_5

number = 35
if number % 3 == 0 and number % 5 == 0:
    print("osztható 3-al és 5-el is")
elif number % 3 == 0:
    print("csak 3-al osztható")
elif number % 5 == 0:
    print("csak 5-el osztható")
else:
    print("nem osztható sem 3-al sem 5-el")

#grades

grade = random.randint(1, 5)
if grade == 5:
    print("Kiválló")
elif grade == 4:
    print("Jó")
elif grade == 3:
    print("Közepes")
elif grade == 2:
    print("elégséges")
elif grade == 1:
    print("elégtelen")
else:
    print("Nem értékelhető")

print(random.random())
