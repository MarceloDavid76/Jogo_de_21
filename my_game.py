

import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


again = True

while again:
    print()
    again = input("Do you want to play? 'y' or 'n':  ")
    if again == 'n':
        again = False
        continue
    else:
        os.system('cls')
        print(logo)
        soma_card_play = [int(random.choice(cards))]
        cards_computer = [int(random.choice(cards))]

        print(f"Your card is: {soma_card_play}")
        print(f"Computer card is: {cards_computer}")
        print()
        another_card = True
        while another_card == True:
            another_card = input("Do you want another card? 'y' or 'n': ")
            if another_card == 'y':
                new_card = int(random.choice(cards))
                print(f"your new card is {new_card}")
                soma_card_play.append(new_card)
                print(soma_card_play)
                sum_s = sum(soma_card_play)
                print(f"Your sum is {sum_s}")
                print()
                if sum_s < 21:
                    another_card = True
                else:
                    print("YOU LOSE")
                    break

            else:
                soma_card_computer = sum(cards_computer)
                while soma_card_computer <= 18:
                    cards_computer.append(int(random.choice(cards)))
                    soma_card_computer = sum(cards_computer)
                print()
                print(f"Cards of computer {cards_computer}")
                print(f"The sum of computer is {soma_card_computer}")
                if soma_card_computer > 21 or (soma_card_computer < sum_s):
                    print("YOU WIN")
                elif sum_s == soma_card_computer:
                    print("A TIE")
                else:
                    print("YOU LOSE")



