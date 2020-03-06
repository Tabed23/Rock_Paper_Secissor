from random import randint


def draw(player, computer):
    return player == computer


def is_win(player, computer):
    if player == 'r' and computer == 'p':
        return 'computer'
    elif player == 'p' and computer == 's':
        return 'computer'
    elif player == 's' and computer == 'r':
        return 'computer'
    elif player == 'r' and computer == 's':
        return 'Player'
    elif player == 'p' and computer == 'r':
        return 'Player'
    elif player == 's' and computer == 'p':
        return 'Player'
    else:
        return 'DRAW'


def main():
    player = input("rock(r) , paper(p) , scissor (s):")
    print(player + ' vs')

    while player != 'q':
        if player == 'q':
            exit()
        chosen = randint(1, 3)
        print(chosen)

        if chosen == 1:
            computer = 'r'
        elif chosen == 2:
            computer = 'p'
        else:
            computer = 's'

        winner = is_win(player, computer)

        print("Winner of this game is  " + str(winner))
        player = input("rock(r) , paper(p) , scissor (s)")


main()
