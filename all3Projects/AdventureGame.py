
from PIL import Image 
import time
import random
# import stuff

username = "" # default username
def wait(f): # to make the opertation wait a certain amount of time
    time.sleep(f)
    s = 1
def gettInput(x, xx):
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
        
    
def Dialogue(s): # types the text out slowly
    if not "?" in s:
        if not "." in s:
            s = s +"."
    
    print(s )
    
    wait(len(s)/17.0)
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
        print("Alright " +x +", lets start your adventure!")
        username = x
        wait(1)
        break
    else:
        print("Names do not match")

def d(s): # to make shorter and easier
    Dialogue(s)

d("You find yourself in a forest") #begin the story
Dialogue("You must choose to walk up or down")

DisplayImage("Forest") # initial
x = gettInput("down", "up")


def Part1(): # second part of game
    Dialogue("A few hours later")
    Dialogue("You see a house in the distant")
    Dialogue("You start running towards it as the sun sets")
    DisplayImage("House")
    Dialogue("Do you choose to enter it?")
    GUN = False
    x = gettInput("no", "yes")
    if x == True: # make sure the x value is true 
        d("Upon opening the door")
        d("You see a dead bodie wearing the same color t-shirt as you")
        d("You reach into your backpack and pull out your iron sword")
        d("You poke the bodie with the sword")
        d("Stab it a few times")
        d("You have confirmed the bodie is dead")
        d("You scan the room to look for any other people...")
        d("Its just you and this dead bodie...")
        d("Do you wish to rob the place?")
        
        x = gettInput("no", "yes")
        if x == True:
            d("You gain "+ str(random.randint(201, 300)) +" dollars, a revolver with 6 bullets and another t-shirt")
            d("Benjamin would've wanted you to have his wallet")
            d("Weak dude")
            GUN = True
        else:
            d("Well said, well said")
        
        d("You exit the house and proceed to walk up the mountain")
    d("As the sun sets, you start sprinting")
    d("An hour later...")
    d("You see a cave")
    DisplayImage("Cave")
    d("What will you do next?")
    x = gettInput("ignore", "enter")
    if x == True: # make srurer game workrkr
        d("You enter the cave and lie down")
        d("-- 12 hours later -- ")
        d("You wake up with the pain in your legs gone and a sense of energy")
        d("Reaching into your backpack, you pull out some tissue")
        d("You wrap it around a stick nearby and fashion a torch")
        d("Upon your descend, you find a treasure chest")
        d("You open it and find stacks of gold bars")
        d("Congradulations, "+ username+"!")
        d("You beat the game!")
        DisplayImage("CaveChest")
        
    else: #AHAHAHA
        d("You spend the next 7 hours spiffling in pain")
        d("As your legs are about to give in from the pain of exhaustion")
        d("You see a dog in the distant")
        d("You approach it, expecting it to not attack")
        d("Turns out you were hallucinating from the pain in your legs")
        d("Its a dire wolf")
        DisplayImage("Direwolf")
        d("What will you do?")
        print("a = try to pet the wolf")
        print("b = run")
        print("c = attack with your sword")
        
        if GUN == True:
            print("d = aim your gun at it")
        x = gettInput(": ").lower()
        if x == "d" and GUN == True:
            d("You pull out the revolver and fire all 6 shells at it")
            d("You suck and miss all the bullets")
            
        DEATH(username)
    
if x == True: # reset the story
    Dialogue("So you chose to walk up the mountain")
    Dialogue("You see a baby fox")
    Dialogue("It appears to be hungry")
    Dialogue("Will you feed it the leftover turkey meat in your pocket?")
    DisplayImage("Fox")
    x = gettInput("no", "yes")
    if x == True: # LEMME OUT 
        Dialogue("The baby fox graciously eats the turkey")
        Dialogue("After a few moments, the baby fox lets its guard down and sleeps near your shoe")
        Dialogue("You pet the baby fox")
        Dialogue("A much larger fox arrives, seemingly angry at the sight of a human near the baby fox")
        Dialogue("You quickly reach into your backpack as the larger fox rushes towards you")
        Dialogue("Pick an action")
        print("a = attack the big fox with your iron dagger-")
        print("b = surrender-")
        print("c = start sprinting up the hill-")
        print("d = close your eyes, stand still, and hope for the best-")
        x = input(": ").lower()
        if (x != "d"):
            DEATH(username)
        else:
            Dialogue("The large fox looks closley at the cowering human")
            Dialogue("After a few minutes of the fox carefully circling you, it looses interest")
            print("NICE")
            Dialogue("You continue scaling up the mountain")
            Part1()
        
    else:
        Dialogue("You ignore the baby fox and proceed walking up")
        Part1()
        
    
else: #IM STUCK IN HERE
    # down the mountain
    Dialogue("You tread slowly down the mountain")
    Dialogue("Slowly but surely, you make it to a river")
    Dialogue("Will you stay here and fish a little bit or continue moving?")
    DisplayImage("River")
    x = gettInput("move", "stay")
    if x == True:
        Dialogue("You catch a mysterious yellow fish with thorns")
        Dialogue("Do you choose to cook and eat it?")
        DisplayImage("Pufferfish")
        x = gettInput("no", "yes")
        if x == False:
            Dialogue("You walk towards the river from which you caught it")
            Dialogue("Your stomach growls...")
            Dialogue("So you decide against your better judgment and walk back")
        Dialogue("You start a small campfire and begin cooking it")
        DEATH(username)
        
    else:# THE SECOND ARC
        Dialogue("You find a fallen over log and decide it is safe enough to walk over")
        Dialogue("Upon half way walking through it, the log snaps")
        Dialogue("Making an almost satisfying crunch")
        Dialogue("You fall through and crash into the river")
        Dialogue("You cant swim")
        DEATH(username)
