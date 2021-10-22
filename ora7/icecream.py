
from easygui import *

msgbox("Hello There!", title="HELLO", ok_button="Hi", image="python_logo.png")


flavor =buttonbox("What is your favourite ice cream flavour?", title="Ice cream",
                           choices=['Vanilla[1]', 'Chocolate[2]', 'Strawberry[3]'], default_choice="Vanilla[1]")
msgbox("You picked " + flavor)
flavor = choicebox("What is your favourite ice cream flavour?", title="Ice cream2",
                   choices=['Vanilla[1]', 'Chocolate[2]', 'Strawberry[3]'], preselect=1)
msgbox("You picked " + flavor)

flavor = enterbox("What is your favourite ice cream flavour?", title="Icecream3", default="Körte")
msgbox("You picked " + flavor)