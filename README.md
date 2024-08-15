KBC (Kaun Banega Crorepati) Console Game

This project is a simple console-based quiz game inspired by the popular game show "Kaun Banega Crorepati" (KBC). Players answer a series of multiple-choice questions, each with four options, to win increasing amounts of virtual money. The game continues until the player either answers all questions correctly or gives an incorrect answer.

Project Overview
The game presents 13 questions to the player. Each question is displayed with four answer options, and the player must select the correct option to proceed. The prize money increases with each correct answer, and there are certain guaranteed prize stages, ensuring that the player wins at least that much even if they answer incorrectly later in the game.

Features
13 questions with increasing difficulty.
Multiple-choice questions with four options.
Progressive prize money: the player earns more as they answer more questions correctly.
Guaranteed prize stages: the player is assured of a minimum amount if they reach certain milestones.
The game ends if the player answers a question incorrectly.

How to Play
Run the Python script.
For each question, the game will display four answer options (labeled 1 to 4).
Type the number corresponding to the correct answer and press Enter.
If your answer is correct, you proceed to the next question and earn the corresponding prize money.
If your answer is incorrect, the game ends, and you receive the prize corresponding to the last guaranteed stage you reached.

Prize Structure
Question Number	Prize Money (in Rs.)
1	10,000
2	20,000
3	40,000
4	80,000
5	1,60,000
6	3,20,000
7	6,40,000
8	12,50,000
9	25,00,000
10	50,00,000
11	1,00,00,000
12	5,00,00,000
13	7,00,00,000

Guaranteed Prize Stages
After Question 4: Guaranteed Rs. 80,000
After Question 7: Guaranteed Rs. 3,20,000
After Question 10: Guaranteed Rs. 50,00,000

Code Overview

Class Structure
Question class:
Holds the question, correct answer option, and the four answer choices.

Core Game Logic
The questions are stored in a list called questionlist.
The game loops through each question, displaying it to the player and accepting input.
If the answer is correct, the player proceeds to the next question.
If the answer is incorrect, the game ends, and the prize corresponding to the last guaranteed stage is awarded.

Sample Code Snippet
for i in range(13):
    print(questionlist[i].name)
    print("1: " + questionlist[i].o1)
    print("2: " + questionlist[i].o2)
    print("3: " + questionlist[i].o3)
    print("4: " + questionlist[i].o4)
    answer = input("Your Answer Option : ")
    if answer == questionlist[i].answer:
        print("Correct answer!")
        amount_won = int(amount_group[i])
        print("You have won Rs." + str(amount_won) + '.00\n')
    else:
        print("Incorrect answer!")
        life = False
        break
        
Prize Calculation
At the end of the game, the player is awarded the amount corresponding to the last guaranteed prize stage they crossed.

How to Run
1. Clone or download the project files.
2. Run the Python script using: python kbc.py
3. Follow the on-screen instructions to play.

Future Enhancements
1. Add more questions to the game for increased variety.
2. Implement lifelines like "50-50", "Phone a Friend", and "Audience Poll".
3. Include a graphical interface instead of console-based interaction.
4. Track the player's progress and save high scores.

Enjoy the game and see if you can win the grand prize of Rs. 7 crores!