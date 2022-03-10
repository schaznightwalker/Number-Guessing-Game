import random

'''
#1 -- Randrange
r = random.randrange(11)                 #limit from 0 to 10
print(r)


#2 -- Randrange (limits)
r = random.randrange(-5, 11)             #limit from -5 to 10
print(r)


#3 -- Randint
r = random.randint(0, 11)                #limit from 0 to 11  ***lower limit and upper limit necessary***
print (r)
'''

#4 -- Actual Code
top_of_range = input("Please type a number: ")

if top_of_range.isdigit() :
        top_of_range = int(top_of_range)
    
        if top_of_range <= 0 :
            print("Please type a number larger than 0 next time.")
            quit()
        
else :
        print("Type a (positive) number next time.")
        quit()
        
random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit() :
        user_guess = int(user_guess)
        
    else :
        print("Please type a (positive) number next time.")
        continue
     
    if user_guess == random_number :
        print("Congratulations! You have successfully guessed the number.")
        print("It took you ", guesses, "guesses.")
        break
    elif user_guess > random_number :
        print("Your prediction is greater than the random number.")
    else :
        print("Your prediction is less than the random number.") 
