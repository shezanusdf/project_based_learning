import random

'''First screen asks for bet amount
then as soon as bet am0ount is entered three options come above 7, below 7 or 7
then you choose
then comes the result of the dice with the section the dice came to
then you check if the player won'''

print('''Lucky 7 is a betting game where a player has to bet on
whether the sum of the two dices rolled will be greater than,
less than or equal to 7.''')
print()
print("Your Starting balance is ", 5000, "mon.")

purse = 5000
while True:
    while True:
        print()
        print('Enter Bet Amount: ')
        betAmt = input('> ')
        if not betAmt.isdecimal():
            print("Enter a valid number!")
        elif int(betAmt) > purse:
            print("Bet amount should be under your budget of", purse, 'mon.')
        else:
            break

    while True:
        print("Choose your bet.")
        print("Press 1, 2 or 3.")
        print("Above 7 (1)") 
        print("exactly 7 (2)")
        print("below 7 (3)")
        numchoice = input("> ")
        if numchoice not in ("1","2","3"):
            print("ERROR!")
        elif not numchoice.isdecimal():
            print("Enter 1, 2 or 3")
        else:
            break

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult = dice1 + dice2
    # Results
    print("The dealer rolls the dice.")
    print('First dice got', dice1, "and the second dice got", dice2)
    print("The dices rolled a ",diceresult)

    # Check if User Won
    if (diceresult > 7 and numchoice == "1") or (diceresult < 7 and numchoice == "3"):
        purse = purse + int(betAmt)
        print("You Won ", betAmt)
        print('Your New Balance is ', purse)
    elif (diceresult == 7 and numchoice == "2"):
        purse = purse + int(betAmt) * 2
        print("You hit the Jackpot!")
        print('Your New Balance is ', purse)
    else:
        purse = purse - int(betAmt)
        print("You Lost!")
    print('Press Y to play again and N to quit')
    choice = input("Enter Y or N: ")
    if choice.upper() == "N":
        break
    elif purse <= 0:
        print("You've got no funds left. Qutting...")
        break


