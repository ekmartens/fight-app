#fight moves by type

import random

moves = ['Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Parry 8', 'Parry 12', 'Duck', 'Leap', 'Jump Back', 'Evade Right', 'Evade Left', 'Punto Reverso', 'Garage Door Parry', 'Corps-a-Corps','Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Duck', 'Evade Right', 'Evade Left', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7']

moves_nodupe = ['Evade Left', 'Garage Door Parry', 'Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Corps-a-Corps', 'Parry 8', 'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12']

attacks = ['Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Head Swipe', 'Thrust Body Left', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right','Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Thrust Body Left', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right']

import random

moves_list = ['Evade Left', 'Garage Door Parry', 'Cut Body Left', 'Cut Leg Left','Cut Head Left', 'Leap', 'Head Swipe', 'Thrust Body Left', 'Corps-a-Corps', 'Parry 8', 'Parry 5', 'Parry 4', 'Parry 7', 'Parry 6', 'Parry 1', 'Parry 3', 'Parry 2', 'Lunge', 'Thrust Body Right', 'Evade Right', 'Duck', 'Jump Back', 'Punto Reverso', 'Lunge & Redouble', 'Cut Head Right', 'Cut Body Right', 'Cut Leg Right', 'Parry 12']

def moves_index(m):
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

def first_move():
    event = random.choice(attacks)
    fighters = ['A', 'B']
    first_attacker = random.choice(fighters)
    return first_attacker + ': ' + event

def end_fight():
    fighters = ['A', 'B']
    last_attacker = random.choice(fighters)
    if last_attacker == 'A':
        last_react = 'B'
    else:
        last_react = 'A'
    final_attack = random.choice(attacks)
    end_attacks_set = set(attacks)
    end_attacks = [end_attacks_set, 'Pasada Soto 1 (Squat)','Pasada Soto 2 (Leg Back)', 'Pasada Soto 3 (Leg Diagonal)']
    if final_attack == 'Pasada Soto':
        end = 'Surrender'
    else:
        end = 'Dramatic Death'
    return last_attacker + ': ' + final_attack + ' -> ' + last_react + ': ' + end

def create_fight(num_moves):
    while num_moves > 100:
        print "That's a really long fight..."
        num_moves = input("How many moves in your fight?")
    else:
        print "En garde!"
        print first_move()
        for num in range(int(num_moves) - 2):
            m = random.choice(moves)
            print moves_index(m)
        print end_fight()
num_moves = input('How many moves in your fight?')
create_fight(num_moves)
