import random,sys
import keyboard 
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han

In this traditional japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number
''')

purse = 5000
while True: # Game loop
    # Place bet
    print('You Have', purse, 'mon. How much do you bet? (or press Esc to QUIT)')
    while True:
        pot = input('> ')
        if keyboard.is_pressed('esc'):
            print("Thanks For Playing!")
            sys.exit()    
        elif not pot.isdecimal():
            print('Please enter a valid number.')
        elif int(pot) > purse :
            print('You do not have enough to make the bet.')
        else:
            # Valid Bet
            pot = int(pot) 
            break # Exit loop once bet placed

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

            
    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('     CHO (even) or HAN (odd)?')                  
    
    # Choose b/w Cho or Han
    while True:
        bet = input('> ').upper()   
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either CHO or HAN')
            continue
        else:
            break

    # Reveal Results