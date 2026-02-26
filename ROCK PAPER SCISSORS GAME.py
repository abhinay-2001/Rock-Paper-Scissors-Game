#!/usr/bin/env python
# coding: utf-8

# # **Description**
The Rock Paper Scissors Game is a console-based application developed using Python programming language. The project is designed to simulate the traditional Rock-Paper-Scissors hand game in a digital format where a user plays against the computer.The main objective of this project is to demonstrate the implementation of Python fundamentals and Object-Oriented Programming (OOP) concepts in a structured and modular way.
# # **Rock Paper Scissors Game**

# In[2]:


# ROCK PAPER SCISSORS GAME

import random

class Player:

    def __init__(self, name):
        self.name = name
        self.__score = 0   

    def get_score(self):
        return self.__score

    def increase_score(self):
        self.__score += 1


class Game:

    def __init__(self, player_name):
        self.player = Player(player_name)
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.player.increase_score()
            return "User"
        else:
            return "Computer"

    def play_round(self):
        user_choice = input("Enter rock, paper, or scissors: ").lower()

        if user_choice not in self.choices:
            print("Invalid choice! Try again.")
            return

        computer_choice = self.get_computer_choice()

        print("Computer chose:", computer_choice)

        result = self.determine_winner(user_choice, computer_choice)

        if result == "Tie":
            print("It's a Tie!")
        elif result == "User":
            print("You Win this round!")
        else:
            print("Computer Wins this round!")

    def start_game(self):
        rounds = int(input("How many rounds do you want to play? "))

        for i in range(rounds):
            print(f"\nRound {i+1}")
            self.play_round()

        print("\n===== Game Over =====")
        print("Your Final Score:", self.player.get_score(), "/", rounds)

print("===== Rock Paper Scissors Game =====")
name = input("Enter your name: ")

game = Game(name)
game.start_game()


# In[ ]:




