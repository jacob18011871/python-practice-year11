score = 0
import time
# ASK THE USER THEIR NAME
name = input ("What is your name? ")
# GREET USER AND INTRODUCE THE QUIZ 
if name == "Mr Scribbles":
    print("That name is awfully familiar...")
if name == "Kingston":
    print("Wow! Its THE Kingston! Youre so cool and handsome and sexy")
if name == "Jack":
    print("MIDGET")
print ("You have a nice name,",name)
print ("Welcome! This quiz is just easy general knowledge! Remember, answers are case sensitive!")
# ASK THE USER QUESTION
answer = input ("Question 1: When did Kaiser Wilhelm I die? ")
# SHOW THEM THE ANSWER
if answer == "1888":
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("You there?")
else:
    print("Incorrect answer! You have lost control of your legs as consequence. -1!")
    print("Kaiser Wilhelm died in 1888!")
    score -= 1

# ASK THE USER QUESTION 2
answer = input ("Question 2: How long did the Cold War last? ")
# SHOW THEM THE ANSWER
if answer == "45 years":
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("Hello? We have a quiz to finish!")
else:
    print("Incorrect answer! You have lost control of your arms as consequence. -1!")
    print("The cold war lasted '45 years'.")
    score -= 1
# ASK THE USER QUESION 3
answer = input ("Question 3: When did the NZ Labour Party first come into power? ")
# SHOW THEM THE ANSWER
if answer == "1935":
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("Where are you? I can't see you!")
else:
    print("Incorrect answer! You have lost your cerebral cortex as consequence. -1!")
    print("The NZ Labour Party first came into power in 1935!")
    score -= 1
# ASK THE USER QUESTION 4
answer = input ("Question 4: Give me the chemical formula for magnesium bromide. ")
# SHOW THEM THE ANSWER
if answer == "MgBr2":
    print("Great job! Thats right! +1")
    score += 1
elif answer == "":
    print("It wasn't that difficult, was it?")
else:
    print("Incorrect answer! You have lost your left lung as consequence. -1!")
    print("The formula is: MgBr2")
    score -= 1
# QUESTION 5
answer = input ("Question 5: What year was television invented? ")
# ANSWER
if answer == "1927":
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("Remember, you have to type something...")
else:
    print("Incorrect answer! Your heart will be sold tomorrow at 3:15pm as consequence. -1!")
    print("Television was invented in 1927!")
    score -= 1
# INTRODUCE DOUBLE POINTS
input ("You've made it halfway! Do you know what that means? ")
print ("Who cares! From now on, you will be EARNING and LOSING double the points! Tread carefully!")
print("Your current score is", score)
if score == 5:
    print("You got all of them correct! I'm so proud of you!")
if score > 4:
    print("You are doing well! Keep up the pace! You got this, good luck!") 
if score == -5:
    print("You got them all incorrect?")
    print("...")
    print("Thats okay. We are all skilled in our own ways. Don't doubt yourself!")
if score < 4:
    print("You fell behind! You gotta try your hardest! I believe in you! Good luck!")

# QUESTION 6
answer = input ("Question 6: How many lights exactly are in the KHCL? ")
# ANSWER
if answer == "155":
    print("Great job! Thats correct! +2!")
    score += 2
elif answer == "":
    print("I know you're there! You need to answer!")
else:
    print("Incorrect answer! Say goodbye to your parents! -2!")
    print("There are 155 lights in the KHCL! (Dont fact check that pwease)")
    score -= 2
# QUESTION 7
answer = input("Question 7: What is the exact date the International Space Station set up? Use this formula: xth of month, 19XX ")
# ANSWER
if answer == "20th of November, 1998":
    print("Great job! Thats right! +2")
elif answer == "":
    print("Just ANSWER the BLOODY QUESTION")
else:
    print("Incorrect answer! You now suffer from stage 5 dementia. -2!")
    print("The ISS was suprisingly launched recently, 20th of November, 1998!")
# QUESTION 8
answer = input("Question 8: The more of me there is, the less you'll see. What am I? ")
# ANSWER
if answer == "Darkness":
    print("Great job! Thats correct! +2!")
    score += 2
elif answer == "":
    print("Listen, I don't know where you're from but where I'M from, we use letters to talk! Not empty space!")
else:
    print("Incorrect answer! Your extended family have been robbed. -2!")
    print("I am darkness! The more you see, the less you see!")
# QUESTION 9
answer = input("Question 9: What is the name of the once supercontinent which broke apart ~200 million years ago? ")
# ANSWER
if answer == "Pangea":
    print("Great job! Thats right! +2!")
    score += 2
elif answer == "":
    print("Just answer the question! Is it that hard!? Can't you do anything right?")
else:
    print("Incorrect answer! Your heart will stop working in five... four... three... -2!")
    print("The once supercontinent was named Pangea!")
    score -= 2
# THE FINAL QUESTION
input("You have made it to... drumroll please... THE FINAL QUESTION! This is it! The gateway to success! Tell me, how do you feel? ")
print("TALKINGS OVER! This is it, the big spin, the jackpot, the FINAL QUESTION! ")
print("...and that question is...")
for i in range(15):
    print("")

answer = input("What are dreams made of? ")
# TRAP ANSWER
if answer == "The unending expansion of the human minds capabilities, dreams are formations of desperate thoughts and memories as your brain attempts to keep itself running, attempting to ignore the fact that the rest of the body could possibly be dead.":
    print("...")
    print("You..")
    suspicion = input("...what did you say your name was again? ")
    if suspicion == "Mr Scribbles":
        print("Its... its really you?")
        

















# END QUIZ