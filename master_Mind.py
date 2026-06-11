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

colors = {
    "1": "red",
    "2": "blue",
    "3": "yellow",
    "4": "green",
    "5": "orange",
    "6": "purple"
}
#dit is een dictionary die cijfers koppelt aan woorden

colors_reverse = {words: number for number, words in colors.items()}
#we zetten het omgedraait zodat woord naar cijfer kan zoeken

hexiwords = list(colors.values())
# lijst van geldige woorden voor de checken en dat ze mogen invoeren

password_admin = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
#dit is een has van het woord password
#voor een nieuw wachtwoord doe dit in terminaal en copy it python3 -c "import hashlib; print(hashlib.sha256('geheim123'.encode()).hexdigest())"

def check_Password(input_password):
    # hash het ingetypte wachtwoord en vergelijk met de opgeslagen hash
    #SHA-256 een wachtwoord om naar een vaste reeks van letters en cijfers
    #.encode() zet tekst naar bytes en .hexdigest() maakt het leesbaar
    input_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_hash == password_admin

user = input('vul je username in:')
password = input('vul je ww in: ') 

def generate_Code(length=4, digits=6):
    return [str(random.randint(1, digits)) for _ in range(length)]
 # makes random codes for the lenghth of array

def get_Feedback(secret, guess):
    black_Pegs = sum(s == g for s, g in zip(secret, guess))
    
    # Count whites by subtracting black and calculating min digit frequency match
    secret_Counts = {}
    guess_Counts = {}

    for s, g in zip(secret, guess):
        if s != g:
            secret_Counts[s] = secret_Counts.get(s, 0) + 1
            guess_Counts[g] = guess_Counts.get(g, 0) + 1

    white_Pegs = sum(min(secret_Counts.get(d, 0), guess_Counts.get(d, 0)) for d in guess_Counts)
    
    return black_Pegs, white_Pegs

def show_Secret(mystery):
    if user == "admin" and check_Password(password):
        print(mystery)

def play_Mastermind():
    print("Welcome to Mastermind!")
    print("Guess the code using colors: red, blue, yellow, green, orange, purple. You have 10 attempts.")
    secret_Code = generate_Code()
    
    attempts = 10

    for attempt in range(1, attempts + 1):
        guess = ""
        valid_Guess = False
        while not valid_Guess:
            
            guess = input(f"Attempt {attempt}: ").strip().lower()
            #vraagt om input
            
            if guess == "hint":
                show_Secret(secret_Code)
                continue
            #anders draait de code niet door want een overdreven gedrag
           
            valid_Guess = guess.lower() in hexiwords
            
            if not valid_Guess:
                print("Invalid input. Enter a color: red, blue, yellow, green, orange, purple")

        guess_as_number = colors_reverse[guess]
        black, white = get_Feedback(secret_Code, [guess_as_number])
        #get_Feedback werkt alleen met cijfers je moet het omdraaien zodat het werkt
        print(f"Black pegs (correct position): {black}, White pegs (wrong position): {white}")

        if black == 1:
            print(f"Congratulations! You guessed the color: {guess}")
            return
    
    print(f"Sorry, you've used all attempts. The correct color was: {[colors[c] for c in secret_Code]}")

if __name__ == "__main__":
    again = 'Y'
    while again == 'Y' :
        play_Mastermind()
        again  = input (f"Play again (Y/N) ?").upper()