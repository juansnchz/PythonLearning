import json
import random

white_possibilities = list(range(1,44))
red_possibilities = list(range(1,17))


tickets_per_drawing = 2 #Número de tiquetes que juego por cada drawing
num_drawings = 104 #2 veces a la semana

total_spent = 0
earnings = 0

results = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "P": 0,
    "0": 0,
}

def calc_win_amt(my_numbers, winning_numbers):
    win_amount = 0
    #How many matches between my chosen white numbers and the winning white numbers
    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    #Is there a powerball match?
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_match:
            win_amount = 18_800_000_000
            results["5+P"] += 1
        else:
            win_amount = 1_300_000_000
            results["5"] += 1

    elif white_matches == 4:
        if power_match:
            win_amount = 7_081_700
            results['4+P'] += 1
        else:
            win_amount = 129_100
            results['4'] += 1
    elif white_matches == 3:
        if power_match:
            win_amount = 42_200
            results["3+P"] += 1
        else:
            win_amount = 12_050
            results['3'] += 1
    elif white_matches == 2 and power_match:
        win_amount = 9_900
        results['2+P'] += 1

    elif power_match:
        win_amount = 5700
        results['P'] += 1
    else:
        results['0'] += 1


    return win_amount

for drawing in range(num_drawings):
    white_draw = set(random.sample(white_possibilities, k=5))
    red_draw = random.choice(red_possibilities)

    winning_numbers = {"whites": white_draw, "red": red_draw}

    for ticket in range(tickets_per_drawing):
        total_spent += int(7800/2)
        my_white_draw = set(random.sample(white_possibilities, k=5))
        my_red_draw = random.choice(red_possibilities)

        my_numbers = {"whites": my_white_draw, "red": my_red_draw}

        win_amt = calc_win_amt(my_numbers, winning_numbers)

        earnings += win_amt



print(f"Spent: ${total_spent}")
print(f"Earnings: ${earnings}")
print(f"Tickets bought: ", tickets_per_drawing*num_drawings )
print(json.dumps(results, indent=2))
