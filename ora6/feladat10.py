import random

is_winner = False
while not is_winner:
    try:
        player = int(input("Kérem adja meg, melyiket mutatja: 1 - kő, 2- papír, 3 - olló\n"))
        bot = random.randint(1,3)
        print(player,bot)
        if player == bot:
            print("Döntetlen")
        elif (player == 2 and bot == 1) or (player == 3 and bot == 2) or (player == 1 and bot ==3):
            print("Nyertél!")
            is_winner = True
        elif (player == 1 and bot == 2) or (player == 2 and bot == 3) or (player == 3 and bot ==1):
            print("Én nyertem.")
            is_winner = True
    except:
        print("Nem megfelelő érték")
