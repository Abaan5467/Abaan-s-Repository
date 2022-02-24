import random
while True:
    x=input("Enter f to flip or e to exit: ")
    side=['Heads','Tails']
    if x== 'f':
        print(random.choice(side))
    elif x=='e':
        break
    else:
        print("Error")