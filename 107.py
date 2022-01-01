#Rock paper scissors

import random

player = str(input('rock paper scissors: '))

computer = random.randint(1,3)

#rock = 1
#Paper = 2
#Scissors = 3

if player == 'rock' and computer == 1:
    print('Draw!')

elif player == 'rock' and computer == 2:
    print ('You lost!')

elif player == 'rock' and computer == 3:
    print ('You win!')

elif player == 'paper' and computer == 1:
    print('You win!')

elif player == 'paper' and computer == 2:
    print ('Draw!')

elif player == 'paper' and computer == 3:
    print ('You lost!')

elif player == 'scissors' and computer == 1:
    print('You lost!')

elif player == 'scissors' and computer == 2:
    print ('You win!')

elif player == 'scissors' and computer == 3:
    print ('Draw!')