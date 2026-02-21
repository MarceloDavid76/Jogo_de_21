
import random
import os

cards = [1, 2, 3, 4, 5, 6, 7, 10, 10, 10]

play = input(f"Do you want to play? y or n?  ")

def escolha_carta():
    return random.choice(cards)

suas_cartas = []
computer_cards = []


while play == "y":
    your_card1 = escolha_carta()
    your_card2 = escolha_carta()
    computer_card1 = escolha_carta()
    computer_card2 = escolha_carta()

    print(f"Suas cartas são [{your_card1}, {your_card2}]")
    suas_cartas.append(your_card1)
    suas_cartas.append(your_card2)

    print(f"Computer first card is: {computer_card1}")
    computer_cards.append(computer_card1)
    computer_cards.append(computer_card2)

    more_cards = input(f"do you want more card? y or n ")

    while more_cards == "y":
        new_card = escolha_carta()
        suas_cartas.append(new_card)
        print(f"Your cards: {suas_cartas}")
        if sum(suas_cartas) > 21:
            print(f"you lose")
            print(f"your final cards is {suas_cartas}, final score {sum(suas_cartas)}")
            print(f"computer cards is {computer_cards}, final score {sum(computer_cards)}")
            break
            
            
        else:
            more_cards = input(f"do you want more card? y or n ")

    if sum(suas_cartas) > 21:
        break
    else:
    
    
        while sum(computer_cards) < 17:
            more_computer_card = escolha_carta()
            computer_cards.append(more_computer_card)

        if (sum(computer_cards) > sum(suas_cartas) and sum(computer_cards) < 22) :
            print(f"you lose")
            print(f"your final cards is {suas_cartas}, final score {sum(suas_cartas)}")
            print(f"computer cards is {computer_cards}, final score {sum(computer_cards)}")

        if sum(computer_cards) < sum(suas_cartas):
            print(f"you win")
            print(f"your final cards is {suas_cartas}, final score {sum(suas_cartas)}")
            print(f"computer cards is {computer_cards}, final score {sum(computer_cards)}")

        if sum(computer_cards) == sum(suas_cartas):
            print(f"empate")
            print(f"your final cards is {suas_cartas}, final score {sum(suas_cartas)}")
            print(f"computer cards is {computer_cards}, final score {sum(computer_cards)}")

    play = input(f"Do you want to play again? y or n?  ")
    os.system('cls')





