import numpy as np

print("Welcome to rock, paper, and scissors")

#user input

user_input=input("select rock, paper, or scissors: ")

#print("you chose: ", user_input)

print(f"you chose: '{user_input}' ")

#validate user input

#computer choice

list1=['rock','paper','scissors']

computer_input=np.random.choice(list1)

print(f"computer chose: '{computer_input}' ")

#determine the winner

if user_input == 'rock':
    num_user = 0
if user_input == 'paper':
    num_user = 1
if user_input == 'scissors':
    num_user = 2

if computer_input == 'rock':
    num_computer = 0
if computer_input == 'paper':
    num_computer = 1
if computer_input == 'scissors':
    num_computer = 2

#rock -- rock
#rock -- paper
#rock -- scissors

#paper -- rock
#paper -- paper
#paper -- scissors

#scissors -- rock
#scissors -- paper
#scissors -- scissors

#display results

#----
#Welcome player one...
#----
#Please choose either rock, paper, or scissors: rock
#You chose rock
#The computer chose paper
#----
#The computer won...
