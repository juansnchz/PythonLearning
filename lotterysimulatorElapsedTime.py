import json
import random

white_possibilities = list(range(1,70))
red_possibilities = list(range(1,27))


tickets_per_drawing = 100 #Número de tiquetes que juego por cada drawing
num_drawings = 156 #3 veces a la semana

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
    "1+P": 0,
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
            win_amount = 2_000_000_000
            results["5+P"] += 1
        else:
            win_amount = 1_000_000
            results["5"] += 1

    elif white_matches == 4:
        if power_match:
            win_amount = 50_000
            results['4+P'] += 1
        else:
            win_amount = 100
            results['4'] += 1
    elif white_matches == 3:
        if power_match:
            win_amount = 100
            results["3+P"] += 1
        else:
            win_amount = 7
            results['3'] += 1
    elif white_matches == 2 and power_match:
        win_amount = 7
        results['2+P'] += 1
    elif white_matches == 1 and power_match:
        win_amount = 4
        results['1+P'] += 1
    elif power_match:
        win_amount = 4
        results['P'] += 1
    else:
        results['0'] += 1


    return win_amount

#for drawing in range(num_drawings):
hit_jp = False
drawings = 0
years = 0
while True:
    drawings += 1
    white_draw = set(random.sample(white_possibilities, k=5))
    red_draw = random.choice(red_possibilities)

    winning_numbers = {"whites": white_draw, "red": red_draw}

    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_white_draw = set(random.sample(white_possibilities, k=5))
        my_red_draw = random.choice(red_possibilities)

        my_numbers = {"whites": my_white_draw, "red": my_red_draw}

        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt
        if win_amt == 2_000_000_000:
            hit_jp = True
            break
    if drawings % 156 == 0:
        years += 1
        print(f"{years} years")
    if hit_jp:
        break


print(f"Spent: ${total_spent}")
print(f"Earnings: ${earnings}")
print(f"Tickets bought: ", tickets_per_drawing*num_drawings )
print(json.dumps(results, indent=2))
