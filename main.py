score = 0
import time
# ASK THE USER THEIR NAME
name = input ("What is your name? ")
# GREET USER AND INTRODUCE THE QUIZ 
if name == "Mr Scribbles":
    print("That name is awfully familiar...")
if name == "kit":
    print("british midget...")
if name == "Kingston":
    print("Wow! Its THE Kingston! Youre so cool and handsome and sexy")
if name == "Jack":
    print("MIDGET")
if name == "jacob":
    print("you taking your own quiz? weak")
print ("You have a nice name,",name)
print ("Welcome! This quiz is just easy general knowledge!")
# ASK THE USER QUESTION
answer = input ("Question 1: When did Kaiser Wilhelm I die? ").lower()
# SHOW THEM THE ANSWER
if answer == "1888".lower():
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 1
else:
    print("Incorrect answer! You have lost control of your legs as consequence. -1!")
    print("Kaiser Wilhelm died in 1888!")
    score -= 1

# ASK THE USER QUESTION 2
answer = input ("Question 2: How long did the Cold War last? ").lower()
# SHOW THEM THE ANSWER
if answer == "45 years".lower():
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 1
else:
    print("Incorrect answer! You have lost control of your arms as consequence. -1!")
    print("The cold war lasted '45 years'.")
    score -= 1
# ASK THE USER QUESION 3
answer = input ("Question 3: When did the NZ Labour Party first come into power? ").lower()
# SHOW THEM THE ANSWER
if answer == "1935".lower():
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 1
else:
    print("Incorrect answer! You have lost your cerebral cortex as consequence. -1!")
    print("The NZ Labour Party first came into power in 1935!")
    score -= 1
# ASK THE USER QUESTION 4
answer = input ("Question 4: Give me the chemical formula for magnesium bromide. ").lower()
# SHOW THEM THE ANSWER
if answer == "MgBr2".lower():
    print("Great job! Thats right! +1")
    score += 1
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 1
else:
    print("Incorrect answer! You have lost your left lung as consequence. -1!")
    print("The formula is: MgBr2")
    score -= 1
# QUESTION 5
answer = input ("Question 5: What year was television invented? ").lower()
# ANSWER
if answer == "1927".lower():
    print("Great job! Thats right! +1!")
    score += 1
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 1
else:
    print("Incorrect answer! Your heart will be sold tomorrow at 3:15pm as consequence. -1!")
    print("Television was invented in 1927!")
    score -= 1
# INTRODUCE DOUBLE POINTS
input ("You've made it halfway! Do you know what that means? ")
print ("Who cares! From now on, you will be EARNING and LOSING double the points!")
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
answer = input ("Question 6: How many lights exactly are in the KHCL? ").lower()
# ANSWER
if answer == "155".lower():
    print("Great job! Thats correct! +2!")
    score += 2
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 2
else:
    print("Incorrect answer! Say goodbye to your parents! -2!")
    print("There are 155 lights in the KHCL! (Dont fact check that pwease)")
    score -= 2
# QUESTION 7
answer = input("What is the most useful painkiller? ").lower()
# ANSWER
if answer == "Naproxen".lower():
    print("Great job! Thats right! +2")
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 2
else:
    print("Incorrect answer! You now suffer from stage 5 dementia. -2!")
    print("The answer is Naproxen... wow!")
# QUESTION 8
answer = input("Question 8: The more of me there is, the less you'll see. What am I? ").lower()
# ANSWER
if answer == "Darkness".lower():
    print("Great job! Thats correct! +2!")
    score += 2
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 2
else:
    print("Incorrect answer! Your extended family have been robbed. -2!")
    print("I am darkness! The more you see, the less you see!")
# QUESTION 9
answer = input("Question 9: What is the name of the once supercontinent which broke apart ~200 million years ago? ").lower()
# ANSWER
if answer == "Pangea".lower():
    print("Great job! Thats right! +2!")
    score += 2
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 2
else:
    print("Incorrect answer! Your heart will stop working in five... four... three... -2!")
    print("The once supercontinent was named Pangea!")
    score -= 2
# THE FINAL QUESTION
input("You have made it to... drumroll please... THE FINAL QUESTION! This is it! The gateway to success! Tell me, how do you feel? ")
print("TALKINGS OVER! This is it, the big spin, the jackpot, the FINAL QUESTION! ")
print("...and that question is...")
for i in range(8):
    print("")

answer = input("If x is the average (arithmetic mean) of 𝑚 and 9, y is the average of 2 𝑚 and 15, and z is the average of 3 𝑚 and 18, what is the average of x, y, and z in terms of 𝑚 ?").lower()
# ANSWER
if answer == "m+7" or answer == "m + 7".lower():
    print("Great job! Thats right! +2")
    score += 2
elif answer == "":
    print("You insult me by not answering my questions.")
    score -= 2
else:
    print("Incorrect answer! Your home country will be ruthlessly bombed. -2!")
    print("The answer is m + 7!")
# GOODBYE
input("Congratulations, you finally finished the quiz! Actually... You know what? Bonus question! What is your final score? ")
if answer == score:
    print("Thats right! Your score is", score, "!")
    print("")

        

















# END QUIZ
# test area







tries = input("balahslasdlbasdlkbas")
tries = tries - 1