while True:
    import random

    user = input("Enter R for rock, P for paper and S for Scissor: ")

    computer_choice=['r','p','s']

    x= random.choice(computer_choice)

    if user =='R' and x =='r':
        print('The computer selected: ',x)
        print('Draw')
    elif user =='P' and x =='r':
        print('The computer selected: ',x)
        print('You Win!!')
    elif user =='S' and x =='r':
        print('The computer selected: ',x)
        print('Computer Won')
    elif user =='R' and x =='p':
        print('The computer selected: ',x)
        print('Computer Won')
    elif user =='R' and x =='s':
        print('The computer selected: ',x)
        print('You Win!!')
    else:
        print('Error')