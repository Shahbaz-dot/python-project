# Welcome to the Snake–Water–Gun Game! 🐍💧🔫
Developed by Mr. Shahbaz ibn Ehfaz, this exciting and fun-filled game brings a classic twist to your screen!
Test your luck, challenge your reflexes, and see who wins — Snake, Water, or Gun!


import random

def check(comp, user):
    if comp == user :
        return 0
    if(comp == 0 and user == 1):
        return -1
    if(comp == 1 and user == 2):
        return -1
    if(comp == 1 and user == 0):
        return -1
        
        return 1
print("🎮 Introducing “Snake-Water-Gun” by Mr Shahbaz ibn Ehfaz, An exciting, fast-paced strategy game where you choose Snake, Water or Gun – each beats one and loses to another. Get ready for quick rounds, smart moves and plenty of fun!")
comp = random.randint(0, 2)
user = int(input("0 for snake, 1 for water and 2 for Gun: "))
score = check(comp, user)
print("You: ", user)
print("Comp: ", user)


if(score == 0):
    print("Its a Draw")
elif (score == -1):
    print("You Lose")
else :
    print("You Won ")

print("Thank You for visting here")
