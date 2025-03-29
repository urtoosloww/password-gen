from random import randint
from random import choice, sample
from gg import game
from os import system

animals = [
    "zebra",
    "horse",
    "alligator",
    "lion",
    "tiger",
    "llama",
    "scorpion",
    "spider",
    "peacock"
]
def login():
    global user
    print("Hello, what is your username?")
    user = input()
    print(f"Hello, {user} lets make a unique password!")
    password = "".join(sample(animals, 2))+str(randint(1,999))
    print(f'PASSWORD: {password}')
    print("-" * 80)
    print("Now, lets enter ur login details")
    user_check = input("username: ")
    while user_check != user:
        print("not ur user, try again")
        user_check = input("username: ")
    print("good, now lets move on to the password")
    password_check = input("password: ")
    while password_check != password:
        print("Try again!")
        password_check = input("password: ")
    print("Good, u r logged in")
    print("-" * 80)
def logged_in():
    print("Now, lets play a guessing game")
    
    game(user)
login()
logged_in()