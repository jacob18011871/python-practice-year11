score = 0
# ASK THE USER THEIR NAME
name = input ("What is your name? ")
# GREET USER AND INTRODUCE THE QUIZ 
if name == "Mr Scribbles":
    print("That name is awfully familiar...")
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
else:
    print("Incorrect answer! Your heart will be sold tomorrow at 3:15pm as consequence. -1!")
    print("Television was invented in 1927!")
    score -= 1
# INTRODUCE DOUBLE POINTS
input ("You've made it halfway! Do you know what that means?")
print ("Who cares! From now on, you will be EARNING and LOSING double the points every question! Tread carefully!")
# QUESTION 6
answer = input ("Question 6: How many lights exactly are in the KHCL? ")
# ANSWER
if answer == "155":
    print("Great job! Thats correct! +2!")
    score += 2
# END QUIZ