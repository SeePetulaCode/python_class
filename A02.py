import time as t
import random as r
import math as m
#
# Name : Petula Pascall
# SSID : 616064
# Assignment #: 2
# Submission Date : 3/6/19
#
# Description of program :
# This is a trivia quiz about the History of Computer Gaming
#
print ("*********************************************************** ")
print ("  Welcome to the History of Computer Gaming Trivia Quiz")
print ("  Win by answering all three questions correctly ")
print ("*********************************************************** ")


score = 0; quiz_length = 2; quiz = 0; active_game = True

# List of questions
q = [

      ["Which decade was the Golden Age of Gaming?","1950s", "2000s", "1980s", "1970s", "3"],
      ["What is the name of the first commercial arcade video game?","Pong", "Computer Space", "Space Invaders", "Pac Man", "2"],
      ["What is the name of the first video game console?", "Atari", "Nintendo Entertainment System", "Sega", "Playstation", "1"],
      ["During the 1960s, what was the name of a computer used by MIT students to play computer games(via punch cards?", "Model K", "IBM Watson", "IBM 1560",
       "IBM 3340", "3"],
      ["What was the name of the first video game created in 1958?","Pong", "Duck Hunt", "Blue's Clues", "Table for Two", "4"],
      ["The game Tetris created by Russian game designer Alexey Pajitnov on:","June 6, 1984", "April 12, 1965", "November 22, 1985", "July 12, 1975", "1"],
      ["Japanese game designer, Shigeru Miyamoto, created the \'Legend of Zelda\' in:","1980", "1985", "1987", "1990", "3"],
      ["What is the name of the first handheld game console that used interchangeable cartridges?","Game Boy", "Microvision", "Game & Watch", "Sega Game Gear", "2"],

    ]

# Shuffle the list of questions to make random
r.shuffle(q)

# Reactions to wrong or right answers
compliments = ["Awesome!", "Great Job!!", "You're Smart!", "You are really smart!", "Excellent!"]
compliments_len = len(compliments) - 1
non_compliments = ["That is incorrect, let's try another question!", "No, but let's try another!", "Better luck next time!", "No, Wrong! Let's Try Another Question. You got this!"]
non_compliments_len = len(non_compliments) - 1

# Game is active
while active_game == True:


    print("Q"+str(quiz+1)+".",q[int(quiz)][0])
    print("1.",q[int(quiz)][1])
    print("2.",q[int(quiz)][2])
    print("3.",q[int(quiz)][3])
    print("4.",q[int(quiz)][4])
    correct = str(q[int(quiz)][5])
    answer = input("Enter your answer(1, 2, 3, or 4): ")


    # If question is correct? Print rx then add to score and place in quiz
    if answer  == correct:
        random_compliment = r.randint(0, compliments_len)
        print(compliments[random_compliment],end="\r\n\r\n")
        score += 1; quiz +=1

    # If question is incorrect? Print rx then add to score and place in quiz
    else:
        random_non_compliment = r.randint(0, non_compliments_len)
        print(non_compliments[random_non_compliment], end="\r\n\r\n")
        quiz += 1

    # If the player answer 1/more of 3 questions wrong? Start over!
    if quiz == quiz_length+1 and score !=3:
        quit_game = input("Do you want to try again? (y)es or (n)o?: ")

        if quit_game == 'y':
            score = 0; quiz = 0

            print("\r\n\r\n*********************************************************** ")
            print("  Welcome to the History of Computer Gaming Trivia Quiz")
            print("  Win by answering all three questions correctly ")
            print("*********************************************************** ")

        elif quit_game == 'n':
            print("Thank you for playing. Goodbye")
            break
        else:
            print("Thank you for playing. Goodbye")
            break

    # If the player answers all 3 questions? End Game!
    if score == 3:
        active_game = False



else:

    print("You won! All three answers were correct!")
    t.sleep(1)
    print("Thank you for playing. Goodbye")


