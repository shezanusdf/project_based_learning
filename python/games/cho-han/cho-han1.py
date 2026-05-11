import random

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}


print('''In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.''')
purse = 5000
while True:
    while True:
        print('You have', purse, 'mon. How much do you bet?')
        pot = (input('> '))
        if not pot.isdecimal():
            print('Enter a valid number')
        elif (int(pot) > purse):
            print('You only have', purse, 'mon. Bet accordingly.')
        else:
            break

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')

    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('> ')
        if bet.upper()!='HAN' and bet.upper()!='CHO':
            print('Enter CHO or HAN')
        else:
            break
        
    #  Results
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print('The dealer lifts the cup to reveal: ')
    print(JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print(dice1, '-', dice2)

    # Check if player Won
    if (dice1 + dice2) % 2 == 0 and bet.upper() == 'CHO':
        print('You Won! You take', pot, 'mon.')
        purse = purse + int(pot)
    elif (dice1 + dice2) % 2 != 0 and bet.upper() == 'HAN':
        print('You Won! You take', pot, 'mon.')
        purse = purse + int(pot)
    else:
        print('You Lost!')
        purse = purse - int(pot)
    print('Press Y to restart and N to quit')
    WantToPlay = input("> ")
    if WantToPlay.upper()!='Y':
        break




