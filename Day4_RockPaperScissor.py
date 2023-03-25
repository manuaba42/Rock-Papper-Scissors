import random

print("Welcome")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

condi = True
while condi == True:
    draw = int(input("0. Rock, 1. Papper, 2. Scissor\n"))

    rando = random.randint(0,2)
    # print(rando)
    if draw == rando:
        if draw == 0:
            print("You : \n")
            print(rock)
            print("Computer : \n")
            print(rock)
        elif draw == 1:
            print("You : \n")
            print(paper)
            print("Computer : \n")
            print(paper)
        elif draw == 2:
            print("You : \n")
            print(scissors)
            print("Computer : \n")
            print(scissors)
        print("Tie!!")
    elif draw == 0 and rando == 1:
        print("You : \n")
        print(rock)
        print("Computer : \n")
        print(paper)
        print("Computer draw papper, You Lose!!")
    elif draw == 0 and rando == 2:
        print("You : \n")
        print(rock)
        print("Computer : \n")
        print(scissors)
        print("Computer draw Scissor, You Win!!")
        condi = False
    elif draw == 1 and rando == 0:
        print("You : \n")
        print(paper)
        print("Computer : \n")
        print(rock)
        print("Computer draw Rock, You Win!!")
        condi = False
    elif draw == 1 and rando == 2:
        print("You : \n")
        print(paper)
        print("Computer : \n")
        print(scissors)
        print("Computer draw Scissor, You Lose!!")
    elif draw == 2 and rando == 1:
        print("You : \n")
        print(scissors)
        print("Computer : \n")
        print(paper)
        print("Computer draw papper, You Win!!")
        condi = False
    elif draw == 2 and rando == 0:
        print("You : \n")
        print(scissors)
        print("Computer : \n")
        print(rock)
        print("Computer draw Rock, You Lose!!")
    else:
        print('No Option')
