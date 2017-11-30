import random

moves_list = ['Evade Left', 'Garage Door Parry', 'Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Corps-a-Corps', 'Parry 8', 'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12', 'React', 'Knee Body Right', 'Knee Body Left', 'Thrust Kick', 'Pommel Strike', 'Elbow Body']

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
        reaction = ['Cut Leg Right', 'Cut Body Right', 'Thrust Body Right']
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
        reaction = ['Cut Leg Left', 'Thrust Leg Left']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Lunge':
        reaction = ['Jump Back/Parry 2', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Jump Back/Parry 2', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Garage Door Parry']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Thrust Body Right':
        reaction = ['Parry 4', 'High Parry 1']
        react = random.choice(reaction)
        return "A: " + m + ' -> B: ' + react
    elif m == 'Evade Right':
        reaction = ['Cut Head', 'Diagonal Head Swipe']
        react = random.choice(reaction)
        return "B: " + react + " -> A: " + m
    elif m == 'Duck':
        reaction = ['Overhead Swipe', 'Cut Head Left', 'Cut Head Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Jump Back':
        reaction = ['Thrust Body Right', 'Thrust Body Left', 'Lunge','Thrust Body Right', 'Thrust Body Left', 'Lunge', 'Ballestra/Lunge']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Punto Reverso':
        reaction = ['High Parry 2/Circle Head', 'Vault Left/Parry 3', 'Vault Right/Parry 4']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Lunge & Redouble':
        reaction = ['Parry 1/Circle Parry 1', 'Parry 1/Parry2', 'Parry 1/Parry 3', 'Parry 1/Parry 4', 'Parry 2/Circle Parry 2', 'Parry 2/Parry 1', 'Parry 2/Parry 3', 'Parry 2/Parry 4', 'Parry 3/Circle Parry 3', 'Parry 3/Parry 4', 'Parry 3/Parry 2', 'Parry 3/Parry 1', 'Parry 4/Circle Parry 4', 'Parry 4/Parry 3', 'Parry 4/Parry 2', 'Parry 4/Parry 1']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Cut Head Right':
        reaction = ['High Parry 3', 'Parry 5', 'Evade Right/Hanging Parry 5']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Cut Body Right':
        reaction = ['Parry 3', 'Parry 3', 'High Parry 1']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Cut Leg Right':
        reaction = ['Parry 2', 'Parry 2', 'Parry 7']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
    elif m == 'Parry 12':
        return 'B: Cut Leg Left -> A: ' + m
    elif m == 'React':
        reaction = ['Knee Body Right', 'Knee Body Left', 'Thrust Kick', 'Pommel Strike', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    else:
        return 'B: ' + m + ' -> A: React'


for moves in moves_list:
    l = moves_index(moves)
    print l
