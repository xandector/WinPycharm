import random
# Fist 0, Scissors 1, Cloth 2


def guess_count(guess):
    if guess == 0:
        return 'Fist'
    elif guess == 1:
        return 'Scissors'
    elif guess == 2:
        return 'Cloth'
    else:
        pass


while True:
    player = int(input('What\'s your guess(Fist 0, Scissors 1, Cloth 2):'))
    comp = int(random.randint(0, 2))
    print('Your Guess is:', guess_count(player), '\nComputer\'s guess is:', guess_count(comp))
    if player == comp:
        print('Draw game!', '\n')
    else:
        if player == 0:
            if comp == 1:
                print('You Won!', '\n')
            else:
                print('You Lost!', '\n')
        elif player == 1:
            if comp == 2:
                print('You Won!', '\n')
            else:
                print('You Lost!', '\n')
        elif player == 2:
            if comp == 0:
                print('You Won!', '\n')
            else:
                print('You Lost!', '\n')
