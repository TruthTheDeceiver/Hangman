reset()
import random

# These lines are for the limbs of the hangman.

def draw_pole():
    penup()
    setposition(70,-90)
    pendown()
    forward(40)
    backward(80)
    forward(40)
    left(90)
    forward(200)
    left(90)
    forward(90)
    left(90)
    forward(20)
    penup()
def draw_head():
    pendown()
    color("red")
    right(-90)
    circle(-20)
    penup()
    right(90)
    forward(40)
def draw_torso():
    pendown()
    forward(55)
    backward(55)
    penup()
def draw_arm1():
    pendown()
    right(45)
    forward(35)
    backward(35)
    left(45)
    penup()
def draw_arm2():
    pendown()
    left(45)
    forward(35)
    backward(35)
    right(45)
    penup()
def draw_leg1():
    forward(55)
    pendown()
    right(30)
    forward(35)
    backward(35)
    left(30)
    penup()
def draw_leg2():
    pendown()
    left(30)
    forward(35)
    backward(35)
    right(30)
    penup()
    speed(0)
    setposition(999,999)

def draw_limb():
    turns = 6
    if turns == 5:
        draw_head()
    elif turns == 4:
        draw_torso()
    elif turns == 3:
        draw_arm1()
    elif turns == 2:
        draw_arm2()
    elif turns == 1:
        draw_leg1()
    elif turns == 0:
        draw_leg2()
        print "You lose!"
        print "The word was " + str(word[0:]) + "."

# These lines are used when a word is selected by the system. It's a lot of Copy & Paste.
# There are twenty possible answers.

guess = ""
result = []
corrected = []

def mexico():
    turns = 6
    if word == "MEXICO":
        while turns > 0:
            if "M" in corrected and "E" in corrected and "X" in corrected and "I" in corrected and "X" in corrected and "O" in corrected or "MEXICO" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "M" or guess == "E" or guess == "X" or guess == "I" or guess == "C" or guess == "O" or guess == "MEXICO" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def england():
    turns = 6
    if word == "ENGLAND":
        while turns > 0:
            if "E" in corrected and "N" in corrected and "G" in corrected and "L" in corrected and "A" in corrected and "N" in corrected and "D" in corrected or "ENGLAND" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "E" or guess == "N" or guess == "G" or guess == "L" or guess == "A" or guess == "N" or guess == "D" or guess == "ENGLAND" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def france():
    turns = 6
    if word == "FRANCE":
        while turns > 0:
            if "F" in corrected and "R" in corrected and "A" in corrected and "N" in corrected and "C" in corrected and "E" in corrected or "FRANCE" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "F" or guess == "R" or guess == "A" or guess == "N" or guess == "C" or guess == "E" or guess == "FRANCE" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def germany():
    turns = 6
    if word == "GERMANY":
        while turns > 0:
            if "G" in corrected and "E" in corrected and "R" in corrected and "M" in corrected and "A" in corrected and "N" in corrected and "Y" in corrected or "GERMANY" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "G" or guess == "E" or guess == "R" or guess == "M" or guess == "A" or guess == "N" or guess == "Y" or guess == "GERMANY" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def belgium():
    turns = 6
    if word == "BELGIUM":
        while turns > 0:
            if "B" in corrected and "E" in corrected and "L" in corrected and "G" in corrected and "I" in corrected and "U" in corrected and "M" in corrected or "BELGIUM" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "B" or guess == "E" or guess == "L" or guess == "G" or guess == "I" or guess == "U" or guess == "M" or guess == "BELGIUM" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def norway():
    turns = 6
    if word == "NORWAY":
        while turns > 0:
            if "N" in corrected and "O" in corrected and "R" in corrected and "W" in corrected and "A" in corrected and "Y" in corrected or "NORWAY" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "N" or guess == "O" or guess == "R" or guess == "W" or guess == "A" or guess == "Y" or guess == "NORWAY" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def denmark():
    turns = 6
    if word == "DENMARK":
        while turns > 0:
            if "D" in corrected and "E" in corrected and "N" in corrected and "M" in corrected and "A" in corrected and "R" in corrected and "K" in corrected or "DENMARK" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "D" or guess == "E" or guess == "N" or guess == "M" or guess == "A" or guess == "R" or guess == "K" or guess == "DENMARK" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def finland():
    turns = 6
    if word == "FINLAND":
        while turns > 0:
            if "F" in corrected and "I" in corrected and "N" in corrected and "L" in corrected and "A" in corrected and "N" in corrected and "D" in corrected or "FINLAND" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "F" or guess == "I" or guess == "N" or guess == "L" or guess == "A" or guess == "N" or guess == "D" or guess == "FINLAND" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def china():
    turns = 6
    if word == "CHINA":
        while turns > 0:
            if "C" in corrected and "H" in corrected and "I" in corrected and "N" in corrected and "A" in corrected or "CHINA" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "C" or guess == "H" or guess == "I" or guess == "N" or guess == "A" or guess == "CHINA" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def indonesia():
    turns = 6
    if word == "INDONESIA":
        while turns > 0:
            if "I" in corrected and "N" in corrected and "D" in corrected and "O" in corrected and "N" in corrected and "E" in corrected and "S" in corrected and "I" in corrected and "A" in corrected or "INDONESIA" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "I" or guess == "N" or guess == "D" or guess == "O" or guess == "N" or guess == "E" or guess == "S" or guess == "I" or guess == "A" or guess == "INDONESIA" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def egypt():
    turns = 6
    if word == "EGYPT":
        while turns > 0:
            if "E" in corrected and "G" in corrected and "Y" in corrected and "P" in corrected and "T" in corrected or "EGYPT" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "E" or guess == "G" or guess == "Y" or guess == "P" or guess == "T" or guess == "EGYPT" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def turkey():
    turns = 6
    if word == "TURKEY":
        while turns > 0:
            if "T" in corrected and "U" in corrected and "R" in corrected and "K" in corrected and "E" in corrected and "Y" in corrected or "TURKEY" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "T" or guess == "U" or guess == "R" or guess == "K" or guess == "E" or guess == "Y" or guess == "TURKEY" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def poland():
    turns = 6
    if word == "POLAND":
        while turns > 0:
            if "P" in corrected and "O" in corrected and "L" in corrected and "A" in corrected and "N" in corrected and "D" in corrected or "POLAND" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "P" or guess == "O" or guess == "L" or guess == "A" or guess == "N" or guess == "D" or guess == "POLAND" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def spain():
    turns = 6
    if word == "SPAIN":
        while turns > 0:
            if "S" in corrected and "P" in corrected and "A" in corrected and "I" in corrected and "N" in corrected or "SPAIN" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "S" or guess == "P" or guess == "A" or guess == "I" or guess == "N" or guess == "SPAIN" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def brazil():
    turns = 6
    if word == "BRAZIL":
        while turns > 0:
            if "B" in corrected and "R" in corrected and "A" in corrected and "Z" in corrected and "I" in corrected and "L" in corrected or "BRAZIL" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "B" or guess == "R" or guess == "A" or guess == "Z" or guess == "I" or guess == "L" or guess == "BRAZIL" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def korea():
    turns = 6
    if word == "KOREA":
        while turns > 0:
            if "K" in corrected and "O" in corrected and "R" in corrected and "E" in corrected and "A" in corrected and "KOREA" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "K" or guess == "O" or guess == "R" or guess == "E" or guess == "A" or guess == "KOREA" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def chile():
    turns = 6
    if word == "CHILE":
        while turns > 0:
            if "C" in corrected and "H" in corrected and "I" in corrected and "L" in corrected and "E" in corrected or "CHILE" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "C" or guess == "H" or guess == "I" or guess == "L" or guess == "E" or guess == "CHILE" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def peru():
    turns = 6
    if word == "PERU":
        while turns > 0:
            if "P" in corrected and "E" in corrected and "R" in corrected and "U" in corrected or "PERU" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "P" or guess == "E" or guess == "R" or guess == "U" or guess == "PERU" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def chad():
    turns = 6
    if word == "CHAD":
        while turns > 0:
            if "C" in corrected and "H" in corrected and "A" in corrected and "D" in corrected or "CHAD" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "C" or guess == "H" or guess == "A" or guess == "D" or guess == "CHAD" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."
def ukraine():
    turns = 6
    if word == "UKRAINE":
        while turns > 0:
            if "U" in corrected and "K" in corrected and "R" in corrected and "A" in corrected and "I" in corrected and "N" in corrected and "E" in corrected or "UKRAINE" in corrected:
                print "---"
                print "You win!"
                print "The word is " + word + "!"
                break
            print "Guesses remaining: " + str(turns)
            print "Incorrect Letters used: " + str(result)
            print "Correct Letters used: " + str(corrected)
            guess = input("Guess: ")
            guess = guess.upper()
            if guess == "U" or guess == "K" or guess == "R" or guess == "A" or guess == "I" or guess == "N" or guess == "E" or guess == "UKRAINE" and guess not in result:
                print "Correct!"
                corrected.append(guess)
            else:
                print "Incorrect!"
                result.append(guess)
                turns = turns - 1
                if turns == 5:
                    draw_head()
                elif turns == 4:
                    draw_torso()
                elif turns == 3:
                    draw_arm1()
                elif turns == 2:
                    draw_arm2()
                elif turns == 1:
                    draw_leg1()
                elif turns == 0:
                    draw_leg2()
                    print "---"
                    print "You lose!"
                    print "The word was " + str(word[0:]) + "."

# These lines are for processing what the player guesses.

speed(9)
draw_pole()
speed(4)
choices = ["MEXICO", "ENGLAND", "FRANCE", "GERMANY", "BELGIUM", "NORWAY", "DENMARK", "FINLAND", "CHINA", "INDONESIA", "EGYPT", "TURKEY", "POLAND", "SPAIN", "BRAZIL", "KOREA", "CHILE", "PERU", "CHAD", "UKRAINE"]
word = random.choice(choices)
print "Your word is " + str(len(word)) + " letters long."

# Word Bank:

mexico()
england()
france()
germany()
belgium()
norway()
denmark()
finland()
china()
indonesia()
egypt()
turkey()
poland()
spain()
brazil()
korea()
chile()
peru()
chad()
ukraine()
