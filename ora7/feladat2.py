import easygui

input_str = easygui.enterbox("Adjon meg egy évszámot: ",title="Adatbekérés")
try:
    ev = int(input_str)
    if ev % 4 == 0:
        if ev % 100 == 0:
            if ev % 400 == 0:
                easygui.msgbox("Ez az év szőkőév.",title="Eredmény")
            else:
                easygui.msgbox("Ez az év nem szökőév.",title="Eredmény")
        else:
            easygui.msgbox("Ez az év nem szökőév.",title="Eredmény")
    else:
        easygui.msgbox("Ez az év nem szökőév.",title="Eredmény")
except ValueError:
    easygui.msgbox("Hibás bemenet",title="Hiba")