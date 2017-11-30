import random

moves_list = ['Evade Left', 'Garage Door Parry', 'Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Corps-a-Corps', 'Parry 8', 'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12']

def moves_index(m):
    # m = random.choice(moves)
    if m == 'Evade Left':
        return 'B: Cut Head Left -> A: ' + m
    elif m == 'Garage Door Parry':
        reaction = ['Thrust Body Left', 'Thrust Body Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Cut Body Left':
        return 'A: ' + m + ' -> B: Parry 3'
    elif m == 'Cut Leg Left':
        return 'A: ' + m + ' -> B: Parry 2'
    elif m == 'Cut Head Left':
        reaction = ['High Parry 3', 'Evade Left/Hanging Parry 6']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Leap':
        reaction = ['Cut Leg Left', 'Cut Leg Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Head Swipe':
        reaction = ['Duck', 'Evade Right/Hanging Parry 5', 'Evade Left/Hanging Parry 6']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Thrust Body Left':
        reaction = ['Parry 2', 'Parry 8']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Corps-a-Corps':
        return 'A/B: ' + m
    elif m == 'Parry 8':
        reaction = ['Cut Body Left', 'Cut Leg Left', 'Thrust Body Left', 'Thrust Leg Left']
        react = random.choice(reaction)
        return 'A: ' + react + ' -> B: ' + m
    elif m == 'Parry 5':
        reaction = ['Cut Head Right', 'Headswipe']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Parry 4':
        reaction = ['Cut Head Right', 'Cut Body Right', 'Thrust Body Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Parry 7':
        reaction = ['Cut Leg Right', 'Cut Body Right', 'Thurst Body Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Parry 6':
        reaction = ['Cut Head Left', 'Headswipe', 'Cut Head']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Parry 1':
        return 'B: Cut Leg Right -> A: ' + m
    elif m == 'Parry 3':
        reaction = ['Cut Body Left', 'Cut Head Left', 'Thrust Body Left']
        react = random.choice(reaction)
        if react == 'Cut Head Left':
            return 'B: ' + react + ' -> A: High ' + m
        else:
            return 'B: ' + react + ' -> A: ' + m
    elif m == 'Parry 2':
        reaction = []

moves_list2 = ['Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12']

for moves in moves_list:
    l = moves_index(moves)
    print l
