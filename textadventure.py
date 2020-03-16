#Jessica Jiang
#jj935@drexel.edu

import time
import random

#reads the user input, stripping and making it lowercase so it is easy to process
def read_input(prompt):
    user_input = input(prompt)
    print()
    user_input = user_input.strip()
    user_input = user_input.lower()
    return user_input

#ends the game and prints a message according to the boolean value of hasWon
def end(hasWon):
    if hasWon:
        print("Congratulations. You have survived the school and escaped!")
    else:
        print("You are now trapped in this school forever... AHAHAHA")
    print("END OF GAME")
    replay_exit = read_input("Would you like to replay or exit?\n")
    if (replay_exit == "replay"):
        play()
    elif (replay_exit == "exit"):
        quit()
    else:
        print("Please type 'replay' or 'exit'.")

#repeat for all teachers and their questions
def Waffer():
    choices = ["A. Tempest", "B. Richard IV", "C. All’s Well That Ends Well", "D. Measure for Measure"]
    print("“Hello there dearie… I am Ms. Waffer. I was an English teacher here at this school. I see that you’re trying to find the key. But I rather you join us in detention. So I’ll strike you a deal. Answer this question and I shall let you pass.”")
    print()
    for i in range(0, len(choices)):
        print(choices[i])

    user_answer = read_input("Which of the above is not a Shakespeare play?\n")

    if (user_answer == "b"):
        print("You are smarter than I thought. The other teachers are not as lenient as me. Good luck I guess.")
    else:
        print("Ah ha ha ha ha haaa. You fool. Richard IV is not one of his plays. You shall be in this school forever now!")
        hasWon = False
        end(hasWon)
def Gill():
    choices = ["A. No Quartering of Soliders in One's Home", "B. Repeal of the 19th Amendment", "C. The President and Vice President are elected together.", "D. Repeal of the 18th Amendment"]
    print("“Hello! I am Mr. Gill. I was the AP Government teacher here at this school. I hope you know your US Constitution.”")
    print("What is the 21st Amendment of the Constitution?")
    for i in range(0, len(choices)):
        print(choices[i])
    user_answer = read_input("")
    if (user_answer == "d"):
        print("Well I guess you do love America. Good luck. I'm not helping you. ")
    else:
        print("Well, straight to dention for you, you uninformed student. Maybe you could learn something there.")
        hasWon = False
        end(hasWon)
def GymTeacher():
    choices = ["A. Pinch Test", "B. Pacer", "C. Curl Ups", "D. Sprinting Across the Gym"]
    print("Strange silence…. BOOM")
    print("You have disturbed the gym teacher.")
    print("'Answer this question now or…. else'")
    print("Which tests is used to determine one’s cardiovascular endurance?")
    for i in range(0, len(choices)):
        print(choices[i])
    user_answer = read_input("")
    if (user_answer == "b"):
        print("“Well you got some knowledge. Move along there.”")
    else:
        print("WRONG! Run 10 laps and then I'm bringing you off to detention!")
        hasWon = False
        end(hasWon)
def Diff():
    choices = ["A. Vosotros", "B. Ustedes", "C. Ella", "D. Nosotros"]
    print("Hola. Me llamo Professora Diff.")
    print("Soy la professora del espanol.")
    print("'Fill in the blank'")
    print("Which of these pronouns is only used in Spain?")
    for i in range(0, len(choices)):
        print(choices[i])
    user_answer = read_input("")
    if (user_answer == "a"):
        print("“Congrats, chic(o/a). Bueno suerte con tu adventura.”")
    else:
        print("Falso! Dentention, it is with you!")
        hasWon = False
        end(hasWon)
def Madame():
    print("Oh No! You've encountered Madame. This won't end well!")
    time.sleep(1)
    print("'HOW DARE YOU BE IN THIS SCHOOL AFTER HOURS!'")
    print("'YOU'RE GOING STRAIGHT TO DETENTION!'")
    print()
    hasWon = False
    end(hasWon)
def Noches():
    print("A ghost has appeared! It is Mr. Noches with a Spanish question for you…")
    print("“I may have been a math teacher in my living days, but I wanted to try something new. So why not Spanish? Answer this question and I give you a hint about where the key is.”")
    user_answer = read_input("What is the Spanish word for milk?")
    if (user_answer == "leche"):
        print("“Good job! Now about the hint. Pick up the note on the ground!”")
    else:
        print("Yeah. Rules are rules. You have to go to detention now.")
        hasWon = False
        end(hasWon)
def Smith():
    print("You enter room 214 and find Ms. Smith who was one of the toughest teachers ever at the school. She has a very hard math question for you.")
    user_answer = read_input("What is the derivative of e^(2*π) / sqrt(3)?")
    if (user_answer == "0"):
        hasWon = True
        end(hasWon)
    else:
        print("You have failed...")
        time.sleep(1)
        hasWon = False
        end(hasWon)

#gets the user's name
def user_name():
    name = input("Welcome! Please input your name.\n")
    return name

#prints the introduction
def print_introduction():
    name = user_name()
    time.sleep(1)
    print()
    print()
    print("Oh No! You suddenly wake up to flickering fluorescent lights. You get up and realize that you’re in school. How did that happen? You quickly run down to the doors and find them all locked. You realized that you have been locked inside the high school. Your cell phone battery is dead, and you’re just met with a black screen. The phone line in the office is dead too. You find a piece of paper of the ground. It says…")
    time.sleep(2)
    print()
    print("______________________________________________________________________________________________")
    time.sleep(1)
    print(" Hello {}.".format(name))
    print()
    time.sleep(1)
    print(" You might have noticed that you’re trapped, alone in the school.")
    time.sleep(1)
    print(" The school is actually haunted by the ghosts of teachers. You must find the key hidden")
    time.sleep(1)
    print(" in one of the classrooms. BUT! Beware. The ghosts are trying to bring to detention for")
    time.sleep(1)
    print(" being here. Answer their questions and you shall pass. Else, you will brought to")
    time.sleep(1)
    print(" for the rest of eternity. God speed on your quest.")
    time.sleep(1)
    print()
    time.sleep(1)
    print()
    print(" -CMJ")
    time.sleep(1)
    print()
    time.sleep(1)
    print("______________________________________________________________________________________________")
    time.sleep(1)
    print()

#moving through the rooms and floor functions   
#intializes the game
def play():
    print_introduction()
    valid1 = False
    input1 = read_input("Would you like to stay on the first floor or go to the second floor? (type 'first' or 'second')\n")
    while (not valid1):
        if (input1 == "first"):
            firstfloorfork()
            valid1 = True
        elif(input1 == "second"):
            print("Oh no the door is locked. Looks like you have to go back down to the first floor for now.\n")
            firstfloorfork()
            valid1 = True
        else:
            input1 = read_input("Type 'first' or 'second'\n")

def firstfloorfork():
    valid_input = False
    input1 = read_input("There is a fork in the hallway do you want to turn Left or Right? (type 'left' or 'right')\n")
    while (not valid_input):
        if (input1 == "left"):
            input2 = read_input("Two rooms are ahead. Room 101 and Room 103. Which one will you enter? (type '101' or '103')\n")
            valid_input = True
            valid2 = False
            while not valid2:
                if(input2 == "101"):
                    Waffer()
                    valid2 = True
                    print("There is so noise coming from room 102. Let's head there.")
                    DocRoom()
                elif (input2 == "103"):
                    Gill()
                    valid2 = True  
                    print("There is so noise coming from room 102. Let's head there.")
                    DocRoom()
                else:
                    input2 = read_input("Type '101' or '103'\n")
        elif(input1 == "right"):
            DocRoom()
            valid_input = True
        else:
            input1 = read_input("Type 'left' or 'right'\n")

def DocRoom():
    time.sleep(1)
    print("Do you hear the people sing...")
    time.sleep(1)
    print("Food Glorious Food...")
    time.sleep(1)
    print("This is our story...")
    time.sleep(1)
    print("Apart of that world...")
    time.sleep(1)
    print()
    print("What beautiful songs. However, it doesn't seem as if any teacher ghosts are appearing nor is the key here. This must be the music room. Oh well. Let's move onto the third floor")
    third_floor()

def third_floor():
    time.sleep(2)
    GymTeacher()
    print("Where you heading now?")
    input1 = read_input("There is two room unlocked ahead. Room 303 and Room 313. Choose to enter one. (type '303' or '313')\n")
    valid1 = False
    while(not valid1):
        if input1 == '303':
            print("There seems to be a lot of tools just lying around. Huh. No signs of anyone or ghosts.")
            print("There's a Captain America Shield on the wall. Other than that, nothing seems out of normal. Let's move on.")
            input2 = read_input("Would you like to go to the fourth floor or enter room 313? (type 'fourth' or '313')\n")
            valid1 = True #exits first loop about entering 303 or 313 initially
            valid2 = False
            while(not valid2):
                if input2 == "fourth":
                    fourthfloor()
                elif input2 == "313":
                    random_val = random.randint(0,10)
                    if random_val % 2 == 0:
                        Diff()
                        valid2 = True
                        print("Let's move onto the fourth floor.")
                        fourthfloor()
                    else:
                        Madame()
                        valid2 = True
                else:
                    input2 = read_input("Type 'fourth' or '313'\n")
        elif input1 == '313':
            random_val = random.randint(0,10)
            if random_val % 2 == 0:
                Diff()
                valid1 = True
                print("Let's move onto the fourth floor.")
                fourthfloor()
            else:
                Madame()
                valid1 = True
        else:
            input1 = read_input("Type '303' or '313'\n")
def fourthfloor():
    print("Looks like there is only one room open. Let's go inside.")    
    time.sleep(1)
    print("There is a note on the ground.")
    input1 = read_input("Do you pick it up? 'Yes' or 'No'\n")
    validfourth = False
    while (not validfourth):
        if input1 == "yes":
            readNote()
            validfourth = True
        elif input1 == "no":
            Noches()
            readNote()
            validfourth = True
        else:
            input1 = read_input("Yes or No\n")
def readNote():
    print("Across the note is the message...")
    time.sleep(2)
    print("------- Go to 214 --------")
    print()
    print()
    print("The key must be there. Let's go now!")
    Smith()

play()