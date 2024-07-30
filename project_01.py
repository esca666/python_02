#Import random and time so that while the game starts computer can pick randomly 
import random
import time
#some introduction :)
print('WELCOME TO THE RSP GAME \n DVELOPED BY ESCA')
print('Game starts in \n...3')
time.sleep(1)
print('...2')
time.sleep(1)
print('...1')

# Because we are making RSP project we are giving 3 choices as below:
choices =['rock','scissor','paper']
time.sleep(2)
while True:
    #letting the player choose pick and as above mentioned computer will pick randomly 
    #thats why we kept import random at first
    user = input('Enter your choice(rock/scissor/paper): ')
    computer = random.choice(choices)
  #putting the condition because while playing RSP there can be only one winner or maybe tie  
    if user ==computer:
            print('Tie')
    elif (user=='rock' and computer=='scissor') or  (user=='scissor' and computer=='paper' )or (user=='paper' and computer=='rock'):
            print('you win')
    else:
            print('You lost')
            break #Putting break because whenever player lose the game it helps to automatically
            #      close the game because nobody likes losing:(
  
#COUNTING USER AND COMPUTER COUNT
    
