'''
    Name: Joey Brosam
    Date: 11/01/18
    Program: Slots
'''

#Setup
import random
bal = 100
bet = 0
fruit = ["Cherries", "Oranges", "Plums", "Bells", "Melons", "Bars"]
reel1 = ""
reel2 = ""
reel3 = ""
winMultipier = 0
wonOrLoss = 0
play = "Y"

#Main Loop
while play == "Y" and bal > 0:
    #Bet Loop
    while bet < 25 or bet > bal:
        bet = int(input("What would you like to bet? ($25 minimum)"))
        if bet < 25:
            print("Bet Below Minimum")
        elif bet > bal:
            print("Your Bet Is Greater Than Your Balance")
    #Pick Fruit For Reels
    reel1 = random.choice(fruit)
    reel2 = random.choice(fruit)
    reel3 = random.choice(fruit)
    print(f"{reel1} | {reel2} | {reel3}")
    #Two Reels Matching
    if reel1 == reel2 or reel2 == reel3:
        print("Two Matching\nYou doubled your bet")
        bal += bet
    #All Reels Matching
    elif reel1 == reel2 and reel2 == reel3:
        print("Three Matching\nYou tripled you bet")
        bal += (bet * 3)
    #No Reels Matching
    else:
        print("None Match\nYou lost your bet")
        bal -= bet
    #Print Balance
    print(f"Remaining Balance:{bal}")
    #Reset Bet
    bet = 0
    #Print Continue Statment Only If Money Remains
    if bal > 0:
        play = input("Input a Y to continue or a n to quit:").upper()
#Exit Thank You Check For Remaining Money
if bal > 0:
    print(f"Thank You For Playing!\nYou ended with ${bal}")
elif bal <= 0:
    print("Thank You For Playing!\nYou lost your money")