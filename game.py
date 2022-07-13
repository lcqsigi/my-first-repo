import numpy as np

print("Welcome to rock, paper, and scissors")

#user input

user_input=input("select rock, paper, or scissors: ")

valid_options = ["rock","paper","scissors"]

#print("you chose: ", user_input)

print(f"you chose: '{user_input}' ")

#validate user input

#computer choice

computer_input=""

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

#rock -- rock      0 0      --> draw
#rock -- paper     0 1      --> paper wins
#rock -- scissors  0 2      --> rock wins

#paper -- rock     1 0      --> paper wins
#paper -- paper    1 1      --> draw
#paper -- scissors 1 2      --> scissors win

#scissors -- rock     2 0   --> rock wins
#scissors -- paper    2 1   --> scissors win
#scissors -- scissors 2 2   --> draw

#display results

if num_user == num_computer:
    print("draw")

if num_user > num_computer and num_user != 0:
    print("you won")

if num_computer > num_user and num_computer != 0:
    print("computer won")

if num_user == 0 and num_computer == 2:
    print("you won")

if num_computer == 0 and num_user == 2:
    print("computer won")

#----
#Welcome player one...
#----
#Please choose either rock, paper, or scissors: rock
#You chose rock
#The computer chose paper
#----
#The computer won...
