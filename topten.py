guesses = []
REACTIVE_METALS_ANSWERS = ["Cesium", "Francium", "Rubidium", "Potassium", "Sodium", "Lithium", "Barium", "Radium", "Strontium", "Calcium"]
# -------- FUNCTIONS --------

# WELCOME THE USER AND INTRODUCE THE QUIZ
def intro():
# ASK THE USER ITS NAME
    name = input("what is your name? ")

# GREET THE USER AND INTRODUCE THE QUIZ
    print("welcome to the quiz", name)
    print("this quiz is about the top ten most reactive METALS in the fancy table about elements!")
# ASK FOR HOW MANY CHANCES THEY WANT
def getLives():
    while True:
        lives = input("How many chances would you like? ")
        try:
            # CHECK IF THE INPUT IS VALID
            lives= int(lives)
            if lives >=0:
                return lives
            else:
                print("You cant have a negative amount of chances, silly!")
        except:
            print("Please use an integer!")
# CHECK IF THE ANSWER ALREADY EXISTS IN THE LIST. USED FOR CHECKING BOTH CORRECT ANSWERS, AND PREVIOUS GUESSES
def isCorrect(answer, list):
    if answer in list:
        return True
    else:
        return False

# -------- MAIN QUIZ --------

intro()
lives = getLives()

score = 0
while lives > 0:
    answer = input("Tell me one of the top 10 most reactive metals in the periodic table: \n").lower()
    # CHECK IF CORRECT
    if inList(answer, REACTIVE_METALS_ANSWERS):
        # CHECK ALREADY GUESSED OR NOT
        if inList(answer, guesses):
            print("You've guessed that before, silly!")
        else:
            print("Correct!")
            score += 5
            guesses.append(answer)
            print("You guessed {}! Your current score is {}... You only have {} chances remaining".format(len(guesses),
        else:
        print("wrong")

        

print("GAME OVER! Your final score is... {}".format(score))
