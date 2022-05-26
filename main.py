import time
import random
import os
import sys


# Highscore
if not os.path.exists("Highscore.txt"):
    
    f = open("Highscore.txt", "w")
    f.write("0")
    f.close()

f = open("Highscore.txt", "r")
Highscore = f.read()
f.close()

print("")
print("Your Highscore is " + Highscore)
print("")


# Some variables that's useful for later on
Game = True
score = 0
text = ()

print("Press 1 to choice the scissors, 2 for the rock and 3 for the paper")
print("")

class GAME:
    
    def __init__(self):
        self.choice_player = (self)
        self.Ia_random = (self)
        self.Result = (self)
        
    # For the randomness of the IA    
    def dice(self):
        self.Ia_random = random.randint(1, 4)
     
    # Choice of the player   
    def player_choice_function(self):
        print("")
        self.choice_player = int(input("Put Your sign here please : "))
            
    # The whole fight
    def Fight(self):
        global text
        
    # For the scissors
        if (self.choice_player) == 1:
            
            if self.Ia_random == 2:
                self.Result = "Lose"
                text = "Your ennemy played a rock"
                
            if self.Ia_random == 3:
                self.Result = "Win"
                text = "Your enemy played the scissors"
                
            if self.Ia_random == 1:
                self.Result = "Equality"
    
    # For the rock
        if self.choice_player == 2:
            
            if self.Ia_random == 3:
                self.Result = "Lose"
                text = "Your ennemy played the paper"
                
            if self.Ia_random == 1:
                self.Result = "Win"
                text = "Your ennemy played the scissors"
                
            if self.Ia_random == 2:
                self.Result = "Equality"
        
    # For the scissors
        if self.choice_player == 3:
            
            if self.Ia_random == 1:
                self.Result = "Lose"
                text = "Your ennemy played the rock"
                
            if self.Ia_random == 2:
                self.Result = "Win"
                text = "Your ennemy played the paper"
                
            if self.Ia_random == 3:
                self.Result = "Equality"
                
    # The text and Highscore to show if you won or not      
    def Text(self):
        global Game
        global score
        global text
        
        print("")
        
        if self.Result == "Lose":
            print("You lose," + text)
            Game = False
            
        if self.Result == "Win":
            print("You Win, " + text)
            print("You can continue to play")
            score += 1
            
        if self.Result == "Equality":
            print("You made a tie")
            print("You need to replay")

obj = GAME()
       
def Da_Game():
    while Game == True:
        obj.player_choice_function()
        obj.dice()
        obj.Fight()
        obj.Text()
        time.sleep(2)
    
Game1 = True

while Game1 == True:
    if Game == True:   
        Da_Game()
        print("")
        
    # New Highscore
    if int(Highscore) < int(score):
        f = open("Highscore.txt", "w")
        f.write(str(score))
        f.close

    # say the score
    print("Your score is " + str(score))
    time.sleep(1)

    # Highscore
    f = open("Highscore.txt", "r")
    Highscore = f.read()
    f.close()

    print("And your Highscore is " + str(Highscore))

    time.sleep(1)

    print("")
    replay = input("Wanna replay ? 1 to replay 2 to quit : ")

    if replay == "1":
        Game = True
        
    if replay == "2":
        Game1 = False
        sys.exit()