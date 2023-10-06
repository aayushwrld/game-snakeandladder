import random

def die_roll1():
    return random.randint(1,6)

def die_roll2():
    return random.randint(1,6)

sandl = {
        1: 38, 4: 14, 9: 31, 16: 6, 21: 42,
        28: 84, 36: 44, 47: 26, 49: 11, 51: 67,
        62: 19, 64: 60, 71: 91, 80: 100, 87: 24,
        93: 73, 95: 75, 98: 78
        }

pos_p1 = 0
pos_p2 = 0

def pos_change(name, position, die):
    pos_updated = position + die
    if pos_updated in sandl:
        if sandl[pos_updated] > pos_updated:
            print(name, "landed on a Ladder 🪜 ! goes up to", sandl[pos_updated])
        elif sandl[pos_updated] < pos_updated:
            print(name, "landed on a Snake 🐍 ! goes down to", sandl[pos_updated])
        return sandl[pos_updated]
    elif pos_updated > 100:
        print(name, "has rolled over 100. Hence staying at the same position. ")
        return position
    else:
        return pos_updated
print("Welcome to Snakes 🐍 and Ladders 🪜! 😄")
input("Press Enter key to start playing!")
name1 = input("Enter name of Player 1  - ")
name2 = input("Enter name of Player 2 - ")

while True:
    input("Press Enter to roll the die 🎲 -> ")

    die1 = die_roll1()
    if die1 == 6:
        temp = 0
        temp = temp + die1
        die1 = die_roll1()
        pos_p1 = temp + pos_p1
        if pos_p1 == 100:
            pass
        else:
            print(name1, "rolled 6!")
            print("Rolling again,", name1, "got", die1)
            pos_p1 = pos_change(name1, pos_p1, die1)
            print(name1, "is now at position", pos_p1)
    else:
        print(name1, "rolled", die1)
        pos_p1 = pos_change(name1, pos_p1, die1)
        print(name1, "is now at position", pos_p1)

    if pos_p1 == 100:
        print(name1, "wins! 👑")
        break

    die2 = die_roll2()
    if die2 == 6:
        temp = 0
        temp = temp + die2
        die2 = die_roll1()
        pos_p2 = temp + pos_p2
        if pos_p2 == 100:
            pass
        else:
            print(name2, "rolled 6!")
            print("Rolling again,", name2, "got", die2)
            pos_p2 = pos_change(name2, pos_p2, die2)
            print(name2, "is now at position", pos_p2)
    else:
        print(name2, "rolled", die2)
        pos_p2 = pos_change(name2, pos_p2, die2)
        print(name2, "is now at position", pos_p2)

    if pos_p2 == 100:
        print(name2, "wins! 👑")
        break
