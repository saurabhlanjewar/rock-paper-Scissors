#  Rock Paper Scissors Game
import random


def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if isWin(user, computer):
        return 'You won!'

    return 'You lost!'


def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print("Rock Paper Scissors Game ")
while True:
    print(play())
    permission = input(" Do Want to continue press y  if not press any key ")[0]
    if permission.upper() == "Y":
        continue
    else:
        print("Thanks for playing")
        break
