#I wrote this code just to play around and test my skils

#Author: Omolola O. Okesanjo
#Creation date: December 10, 2019



print("Welcome to the Number Guessing game!!")
x = input('Press 1 to play, press 2 for instructions, press 3 to exit')

x = int(x)

if x == 2:
    print("The computer will pick a number within the specified range that you give it. Try to predict the computer's number. If you didn't get the number but you are close to getting it, the computer will give you a second try; If not, you fail!")
    y = input("Preass 1 to play or 3 to exit")
    x = int(y)
if x == 3:
    exit

if x == 1:
    num_range = int(input("What is the range you want to guess from?"))
    #To import random module
    import random
    rnumb = random.randrange(num_range)
    your_numb = int(input('Please type a number from 0 to ' + str(num_range)))
    diff = your_numb - rnumb
    diff = abs(diff)
    tolerance = int(num_range * 0.45)
    if diff == 0:
        print('Hooray!! You Win; The number was ' + str(rnumb))
    elif diff <= tolerance:
        print("You're within range, I'll give you one last chance")
        last_chance = int(input())
        diff2 = last_chance - rnumb
        if abs(diff2) == 0:
             print('Hooray!! You Win')
        else:
            print("Sorry, Better luck next time! " + "The number was " + str(rnumb))
    else:
        print("You fail!!!" + "The number was " + str(rnumb))



