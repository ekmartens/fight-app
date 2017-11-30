#fight moves by type

import random

moves = ['Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Parry 8', 'Parry 12', 'Duck', 'Leap', 'Jump Back', 'Evade Right', 'Evade Left', 'Punto Reverso', 'Garage Door Parry', 'Corps-a-Corps', 'Envelope','Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Lunge & Redouble', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Duck', 'Evade Right', 'Evade Left', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7', 'Cut Head Right', 'Cut Head Left', 'Cut Body Right', 'Cut Body Left', 'Cut Leg Right', 'Cut Leg Left', 'Thrust Body Right', 'Thrust Body Left', 'Head Swipe', 'Lunge', 'Parry 1', 'Parry 2', 'Parry 3', 'Parry 4', 'Parry 5', 'Parry 6', 'Parry 7']

ending = ['Pasada Soto 1 (Squat)', 'Pasada Soto 2 (Leg Back)', 'Pasada Soto 3 (Leg Side)', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death', 'Fighter A Dramatic Death', 'Fighter B Dramatic Death']

def create_fight(num_moves):
    while num_moves > 100:
        print "That's a really long fight..."
        num_moves = input("How many moves in your fight?")
    else:
        print "En garde!"
        for num in range(int(num_moves)):
            print(random.choice(moves))
        print(random.choice(ending))
num_moves = input('How many moves in your fight?')
create_fight(num_moves)
