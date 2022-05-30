import time
import random
import os
import sys

print("")

used = False

# Highscore + unlock
if not os.path.exists("Highscore.txt") or not os.path.exists("unlock.txt") :
    
    f = open("Highscore.txt", "w")
    f.write("0")
    f.close()
    
    f = open("unlock.txt", "w")
    f.write("False")
    f.close


f = open("Highscore.txt", "r")
Highscore = f.read()
f.close()

f = open("unlock.txt", "r")
first_unlock = f.read()
f.close()

if first_unlock == "False":
    first_unlock = False
    use_unlock = False
    
else:
    use_unlock = input("Would you like to play with the well ? (1 for Yes, 2 for No) : ")
    
    if use_unlock == "1":
        use_unlock = True
        
    if use_unlock == "2":
        use_unlock = False

print("")
print("Your Highscore is " + Highscore)
print("")


# Some variables that's useful for later on
Game = True
score = 0
text = ()
useless = 1

if use_unlock == False:
    print("Press 1 to choice the scissors, 2 for the rock and 3 for the paper")
    
if use_unlock == True:
    print("Press 1 to choice the scissors, 2 for the rock, 3 for the paper and 4 for the well")
    
    
print("")

class GAME:
    
    def __init__(self):
        self.choice_player = (self)
        self.Ia_random = (self)
        self.Result = (self)

    # For the randomness of the IA    
    def dice(self):
        if use_unlock == False:
            self.Ia_random = random.randint(1, 4)
        if use_unlock == True:
            self.Ia_random = random.randint(1, 5)
     
    # Choice of the player   
    def player_choice_function(self):
        print("")
        
        try:
            self.choice_player = int(input("Put Your sign here please : "))
        except: 
            print("")
            self.choice_player = int(input("please enter an numeric vallue : "))
            
        if use_unlock == False:
            if self.choice_player > 3 or self.choice_player < 0:
                self.choice_player = int(input("please enter an numeric vallue between 1 and 3 : "))
                
        if use_unlock == True:
            if self.choice_player > 4 or self.choice_player < 0:
                self.choice_player = int(input("please enter an numeric vallue between 1 and 4 : "))
            
    # The whole fight
    def Fight(self):
        global text
        
        if use_unlock == False:
            
        # For the scissors
            if (self.choice_player) == 1:
                
                if self.Ia_random == 2:
                    self.Result = "Lose"
                    text = "Your ennemy played the rock"
                    
                if self.Ia_random == 3:
                    self.Result = "Win"
                    text = "Your enemy played the scissors"

        
        # For the rock
            if self.choice_player == 2:
                
                if self.Ia_random == 3:
                    self.Result = "Lose"
                    text = "Your ennemy played the paper"
                    
                if self.Ia_random == 1:
                    self.Result = "Win"
                    text = "Your ennemy played the scissors"

            
        # For the scissors
            if self.choice_player == 3:
                
                if self.Ia_random == 1:
                    self.Result = "Lose"
                    text = "Your ennemy played the rock"
                    
                if self.Ia_random == 2:
                    self.Result = "Win"
                    text = "Your ennemy played the paper"

        if use_unlock == True:
            
            # For the scissors
            if (self.choice_player) == 1:
                
                if self.Ia_random == 2 or 4:
                    self.Result = "Lose"
                    if self.Ia_random == 2:
                        text = "Your ennemy played the rock"
                    if self.Ia_random == 4:
                        text = "Your ennemy played the well"
                    
                if self.Ia_random == 3:
                    self.Result = "Win"
                    text = "Your ennemy played the paper"

        
        # For the rock
            if self.choice_player == 2:
                
                if self.Ia_random == 3 or 4:
                    self.Result = "Lose"
                    if self.Ia_random == 3:
                        text = "Your ennemy played the paper"
                    if self.Ia_random == 4:
                        text = "Your ennemy played the well"
                    
                if self.Ia_random == 1:
                    self.Result = "Win"
                    text = "Your ennemy played the scissors"
                    
            
        # For the paper
            if self.choice_player == 3:
                
                if self.Ia_random == 1:
                    self.Result = "Lose"
                    text = "Your ennemy played the scissors"
                    
                if self.Ia_random == 2 or 4:
                    self.Result = "Win"
                    if self.Ia_random == 2:
                        text = "Your ennemy played the rock"
                    if self.Ia_random == 4:
                        text = "Your ennemy played the well"
                    
                    
        # For the well
        
            if self.choice_player == 4:
                
                if self.Ia_random == 1:
                    self.Result = "Win"
                    text = "Your ennemy played the scissors"
                    
                if self.Ia_random == 2:
                    self.Result = "Win"
                    text = "Your ennemy played the rock"
                    
                if self.Ia_random == 3:
                    self.Result = "Lose"
                    text = "Your ennemy played the paper"

            
          
    # The text and Highscore to show if you won or not      
    def Text(self):
        global Game, score, text, useless
        
        print("")
        
        if self.Result == "Lose":
            print("You lose, " + text)
            Game = False
            
        if self.Result == "Win":
            print("You Win, " + text)
            print("You can continue to play")
            score += 1
        
        if useless == 1:    
            if self.choice_player == self.Ia_random:
                print("You made a tie")
                print("You need to replay")
                useless = 0

obj = GAME()
       
def Da_Game():
    while Game:
        obj.player_choice_function()
        obj.dice()
        obj.Fight()
        obj.Text()
        time.sleep(2)
        
        obj.Result = ()
        obj.Text()
    
Game1 = True

while Game1:
    while Game:   
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

    
    if int(Highscore) >= 5 and first_unlock == False:
        print("You've unlock the secret mode you can now play with the well")
        unlock = str(input("press 1 to play with it and press 2 to not : "))
        
        use_unlock == True
            
        f = open("unlock.txt", "w")
        f.write("True")
        f.close()
            
        if unlock == "1":
            Game = True
            score = 0
            
        if unlock == "2":
            sys.exit
            
        if unlock != "1" and "2":
            time.sleep(1)
            unlock = str(input("Please enter 1 or 2 in an numerical way only"))
            
            if unlock == "1":
                Game = True
                score = 0
        
            if unlock == "2":
                sys.exit
            

    replay = str(input("Wanna replay ? 1 to replay 2 to quit : "))

    if replay == "1":
        
        use_unlock = input("Would you like to play with the well ? (1 for Yes, 2 for No) : ")
            
        if use_unlock == "1":
            use_unlock = True
                
        if use_unlock == "2":
            use_unlock = False
                
        Game = True
        score = 0        

        Game = True
        score = 0
        
    if replay == "2":
        sys.exit()
        
    if replay != "1" and "2":
        time.sleep(1)
        print("Please enter 1 or 2 in an numerical way only")
        
        replay = input("Wanna replay ? 1 to replay 2 to quit : ")
        
        if replay == "1":
            
            use_unlock = input("Would you like to play with the well ? (1 for Yes, 2 for No) : ")
            
            if use_unlock == "1":
                use_unlock = True
                
            if use_unlock == "2":
                use_unlock = False
                
            Game = True
            score = 0
            
        
        if replay == "2":
            sys.exit()