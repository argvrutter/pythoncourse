#number guessing program
import random
answer = random.randint(1,20) 
guessesTaken = 0
guess = 0
print ('I am thinking of a number between 1 and 20.')
while guessesTaken <= 6 and guess != answer:
    print('Take a guess')
    guess = int(input())
    guessesTaken = guessesTaken + 1
    if guess > answer:
        print ('Lower')
    elif guess < answer:
        print ('Higher')
    
if guess == answer:
    print('You got it right! It took you ' + str(guessesTaken) + ' guesses.')
else:
    print('The answer was ' + str(answer))
