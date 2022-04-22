

from PIL import Image
import time
import random
# import stuff

username = "" # default username
def wait(f): # to make the opertation wait a certain amount of time
    time.sleep(f)
def gettInput(answer):
    x = "a"
    xx = "b"
    xxx = "c"
    xxxx = "d"
    global percent
    
    print("Type " +x +", "+xx+ ", "+ xxx+ ", or "+ xxxx)
    
    y = ""
    while y == "":
        y = input(": ").lower()
        if y != x and y != xx and y != xxx and y != xxxx:
            y = ""
            print("Invalid Response")
            print("Type " +x +", "+xx+ ", "+ xxx+ ", or "+ xxxx)
        else:
            if y == answer:
                y = True
                d("Correct")
                percent = percent +1
            else:
                y = False
                d("Incorrect, the answer was "+ answer)
                
    return y
def gettInput1(x, xx):
    x = x.lower()
    xx = xx.lower()
    print("Type " +xx +" or "+x)
    
    y = ""
    while y == "":
        y = input(": ").lower()
        if y != x and y != xx:
            y = ""
            print("Invalid Response")
            print("Type " +xx +" or "+x)
        elif y == x:
            y = False
        else:
            y = True
    return y
def DisplayImage(x): # ment for debugging the project
    if True:
        x = x +".jpg"
        
        x = Image.open(x)
        x.show()
        x.close()
    
def Dialogue(s): # types the text out slowly
    if not "?" in s:
        if not "." in s:
            s = s +"."
    
    print(s )
    
def d(s):
    Dialogue(s)
def DEATH(s): # means you lost the game
    
    Dialogue("Im so sorry "+ s +".")
    DisplayImage("DEATH")


ints = []
for i in range(10): # settup the numbers
    ints.append(str(i))

while True: # settup the game
    print("Enter your name")
    x = input(": ")
    print("Enter again")
    xx = input(": ")
    if xx == x:
        for i in range(len(ints)):
            if ints[i] in xx:
                print("You cannot have numbers in your name -.-")
                wait(3)
                continue
        username = x
        wait(1)
        break
    else:
        print("Names do not match")

d("Want to do an age guess test?")
d("What i do is ask you 10 questions")
d("Then i guess your age based on the answers")

age = 26
percent = 0
x = gettInput1("no", "yes")
if x == True:
    d("What country used the enigma machine to encode messages?")
    print("a = Germany")
    print("b = France")
    print("c = England")
    print("d = Japan")
    
    DisplayImage("Enigma")
    x = gettInput("a")
    
    
    d("If you could tell one peice of advice to yourself in 2002?")
    d("What would it be?")
    print("a = Study hard in school")
    print("b = Today's date and the lottery numbers")
    print("c = Buy as much bitcoin as you possibly can")
    print("d = None of the above")
    x = gettInput("c")
    
    
    d("What is the strongest pokemon")
    print("a = Squirtle")
    print("b = Charizard")
    print("c = Pikachu")
    print("d = What is pokemon?")
    x = gettInput("d")
    
    
    
    d("When was the first computer invented?")
    print("a = 1822")
    print("b = 1993")
    print("c = 2014")
    print("d = 1862")
    x = gettInput("a")
    
    
    d("How many calories does Requis Unchained burn a day?")
    print("a = 2000")
    print("b = 3000")
    print("c = 4000")
    print("d = OVER 9 THOUSAND")
    x = gettInput("d")
    
    
    
    d("EXACTLY, How many bullets from a revolver does it take to kill a bear")
    print("a = 3")
    print("b = 14")
    print("c = 69")
    print("d = 300")
    DisplayImage("Direwolf")
    x = gettInput("c")
    
    
    d("How much money does it take to bribe an american judge")
    print("a = 400 dollars")
    print("b = 6700 dollars")
    print("c = 10020 dollars")
    print("d = 1 million")
    x = gettInput("b")
    
    
    d("Is the ignorance of law a good defense in the court of law?")
    print("a = Always yes")
    print("b = Always No")
    print("c = Depends on your age")
    print("d = Depends on the actions")
    x = gettInput("a")
    
    
    
    d("How many times can the average mouse click before breaking?")
    print("a = 1 thousand")
    print("b = 10 thousand")
    print("c = 100 thousand")
    print("d = 1 million")
    x = gettInput("c")
    
    
    d("Guess how much this car costed me")
    DisplayImage("Car")
    print("a = 4 thousand")
    print("b = 7 thousand")
    print("c = 13 thousand")
    print("d = You are the car")
    x = gettInput("d")
    
    d("You finished the test")
    d("You got "+ str(percent) +" answers correct")
    d("It was out of 10")
    
    percent = percent *10
    d("" +str(percent) +"% ")
    print("Not bad")
else:
    d("Fine, dont help me")
