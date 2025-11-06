import random as rd

class Card:
    def __init__(self, name, attributes, amount):
        self.name = name
        self.attributes = attributes
        self.amount = amount


if __name__ == "__main__":
    playerHP = 100
    botHP = 100
    round = 1

    c1 = Card("Damage", "Burst", 31)
    c2 = Card("Poison", "Debuff", 5)
    c3 = Card("Defense", "Heal", 23)
    c4 = Card("Buff", "Double Effect", 0)

    card_list = [c1, c2, c3, c4]
    
    while True:
        a = rd.choice(card_list)
        b = rd.choice(card_list)
        c = rd.choice(card_list)

        print(f"----------------------------------------------\nROUND {round}")
        print("YOUR CURRENT HP: {hpPlayer}        BOT CURRENT HP: {hpBot}\n----------------------------------------------\n")

    

