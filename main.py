# you are on a game show and are shown three doors.
# behind one of the doors is a large sum of money.
# the other two doors hide goats.
# you are asked to pick a random door.
# after selecting a door, the gameshow host removes one of the losing goat doors.
# you are now left with the door you chose and one other door.
# the game show host asks if you'd like to change doors.
# do you change doors? why or why not?


import random

choices = ['Win', 'Goat', 'Goat']
tries = 1000000
wins = 0
loses = 0

# we conduct a large number of trials (1,000,000).
for i in range(0, tries):

    # the doors are shuffled.
    random.shuffle(choices)

    # we randomly select a door.
    guess = random.choice([0, 1, 2])

    if choices[guess] == 'Win':
        # we originally selected the winning door (1/3 chance).
        # one of the two losing goat doors are removed.
        # we switch doors to the remaining losing goat door, and subsequently lose :(
        # again, there is only a 1/3 chance of this happening.
        loses += 1
    else:
        # we originally select one of the two losing goat doors (2/3).
        # the only other losing goat door is removed.
        # we switch doors to the only remaining door; the winning door.
        # since we have a 2/3 chance of selecting a losing door
        # and since the other losing door is removed,
        # we now have a 2/3 chance of winning when we switch.
        wins += 1

# by switching doors, we flip the odds.
# what was a 2/3 chance of losing is now a 2/3 chance of winning.
# therefore you always switch doors.
print(str(round((wins/tries) * 100, 2)) + '%')
