# My-projects
#a guess the number game
import random,sys
print("Hello! What's your name?")
name=input()
def game():
    secnum=random.randint(1,10)
    print("Well,"+str(name)+" I am thinking of a number between 1 and 20")
    print('Try to guess it within 6 tries')
    for guesses in range(1,7):
        print("Your guess "+ str(guesses)+":")
        guess=int(input())
        if guess<secnum:
            print("Try a higher number")
        elif guess>secnum:
            print("Try a lower number")
        else:
            break;
    if guess==secnum:
        print('Good job '+str(name)+'! You guessed it right')
    else:
        print('Nope! The number I was thinking was '+ str(secnum))
    print('Do you want to try again? Reply with Yes or No')
    inp=str(input())
    if inp=='Yes':
        game()
    else:
        sys.exit()
game() 
