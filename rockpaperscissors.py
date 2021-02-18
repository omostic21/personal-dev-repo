#This is a code for Rock Paper Scissors
print("Welcome to Rock paper Scissors!")
option1 = int(input("Please press 1 for instructions, 2 to play and 3 to exit"))
if option1 == 1:
    print("Fuck off, Instructions will come later, and if you don't know how to play this game..then wtf")
elif option1 == 2:
    print("1 is for rock, 2 is for scissors, 3 is for paper")
    option2 = int(input("Please enter your option"))
    import random
    x = random.randrange(1, 3)
    x = str(x)
    print("I choose " + x)
    x = int(x)
    if option2 == 1 and x == 2:

       print("You win, rock breaks scissors")
    elif option2 == 1 and x == 3:
         
       print("You lose, paper covers rock")
    elif option2 == 2 and x == 1:
        
       print("You lose, rock breaks scissors")
    elif option2 == 2 and x == 3:
         
       print("You win, scissors cuts paper")
    elif option2 == 3 and x == 1:
         
       print("You win, paper covers rock")
    elif option2 == 3 and x == 2:
        
       print("You lose, scissors cuts paper")
    elif option2 == x:
        print("Draw Game")