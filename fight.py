#fight moves by type

import random

moves = ['Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Parry 8', 'Parry 12', 'Duck', 'Leap', 'Jump Back', 'Evade Right', 'Evade Left', 'Punto Reverso', 'Garage Door Parry', 'Corps-a-Corps','Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Duck', 'Evade Right', 'Evade Left', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7']

moves_nodupe = ['Evade Left', 'Garage Door Parry', 'Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Corps-a-Corps', 'Parry 8', 'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12']

attacks = ['Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right']

ending = ['Pasada Soto 1 (Squat)', 'Pasada Soto 2 (Leg Back)', 'Pasada Soto 3 (Leg Side)', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death']

def moves_index(m):
    # m = random.choice(moves)
    if m == 'Evade Left':
        return 'B: Cut Head Left -> A: ' + m
    elif m == 'Garage Door Parry':
        reaction = ['Thrust Body Left', 'Thrust Body Right']
        react = random.choice(reaction)
        return 'B: ' + react + ' -> A: ' + m
    elif m == 'Cut Body Left':
        return: 'A: ' + m + ' -> B: Parry 3'
    elif m == 'Cut Leg Left':
        reaction = ['Parry 2', 'Parry 8']
        react = random.choice(reaction)
        return 'A: ' + m + ' -> B: ' + react
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


     'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12'

def first_move():
    return random.choice(attacks)

def create_fight(num_moves):
    while num_moves > 100:
        print "That's a really long fight..."
        num_moves = input("How many moves in your fight?")
    else:
        print "En garde!"
        print first_move()
        for num in range(int(num_moves) - 2):
            print moves_index()
        print(random.choice(ending))
#num_moves = input('How many moves in your fight?')
#create_fight(num_moves)
