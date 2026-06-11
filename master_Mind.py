#!/bin/python3
# MasterMind
# by ICTROCN
# v1.01
# 15-8-2024
# Last mod by DevJan : added loop for replay
print("MasterMind")

import random
import hashlib
#import de hash

password_admin = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
#dit is een has van het woord password
#voor een nieuw wachtwoord doe dit in terminaal en copy it python3 -c "import hashlib; print(hashlib.sha256('geheim123'.encode()).hexdigest())"

def check_Password(input_password):
    # hash het ingetypte wachtwoord en vergelijk met de opgeslagen hash
    # SHA-256 zet een wachtwoord om naar een vaste reeks van letters en cijfers
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == password_admin

user = input('vul je username in:')
password = input('vul je ww in: ') 

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]
 # makes random codes for the lenghth of array

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    # alleen admin met juist wachtwoord kan de code zien
    if user == "admin" and check_Password(password):
        print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the 4-digit code. Each digit is from 1 to 6. You have 10 attempts.")
    secret_Code = generate_Code()
    
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            guess = input(f"Attempt {attempt}: ").strip()
            valid_Guess = len(guess) == 4 and all(c in "123456" for c in guess)
            if not valid_Guess:
                print("Invalid input. Enter 4 digits, each from 1 to 6.")
            
        black, white = get_Feedback(secret_Code, guess)
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 4:
            print(f"Congratulations! You guessed the code: {''.join(secret_Code)}")
            return

    print(f"Sorry, you've used all attempts. The correct code was: {''.join(secret_Code)}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()