# snake water and gun is a variation of the childrens game rock paper scissors where players use hand gestures to reprsnt a snake, water, or a gun. the gun beats, the water beats the gun and the snake beats the water

#                S W G
# computer =    -1 0 1
# player = S -1  D W L
#          W  0  L D W
#          G  1  W L D


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