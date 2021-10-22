from easygui import *
import random


title= "Számkitaláló"
number = random.randint(1,100)
back = 6
msgbox("Gondoltam egy számra 1-99 között. 6 próbálkozásod van.",
       ok_button="Induljon a játék!")
won = False
hint = ""
while not won and back > 0:
    guess = enterbox(f"{hint} Még {back} próbálkozásod maradt. \n kérem a tipped: ")
    if guess is not None:
        back -= 1
        try:
            guess_number = int(guess)
            if guess_number == number:
                msgbox("Gratulálok, nyertél")
                won = True
            elif guess_number < number:
                hint ="Nagyobb számra gondoltam"
            else:
                hint ="Kisebb számra gondoltam"
        except ValueError:
            msgbox("Byeeee")
if not won:
    msgbox(f"Sajnálom, vesztettél!Én a {number} gondoltam")
tipp = enterbox("Tippelj a számra!")