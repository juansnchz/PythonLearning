import json
import random

loteria1_posibilidades = list(range(0,10000))
loteria2_posibilidades = list(range(0,10000))


tickets_per_drawing = 25 #Número de tiquetes que juego por cada drawing
num_drawings = 365 #Todos los días

total_spent = 0
earnings = 0

results = {
    "Gran_premio": 0,
    "Un_acierto": 0,
    "Nada": 0,
}

def calc_win_amt(mis_numeros, winning_numbers):
    win_amount = 0
    #¿Hubo aciertos en cada una de las loterías?
    aciertos_l1 = len(mis_numeros.intersection(winning_numbers["Loteria1"]))
    aciertos_l2 = len(mis_numeros.intersection(winning_numbers["Loteria2"]))

    if aciertos_l1 == 1 and aciertos_l2 == 1:
        results["Gran_premio"] += 1
        win_amount += 1_000_000_000

    if (aciertos_l1 == 0 and aciertos_l2 == 1) or (aciertos_l2 == 0 and aciertos_l1 == 1):
        results["Un_acierto"] += 1
        win_amount += 1_260_000
        print("Mis números fueron: ", mis_numeros)
        if aciertos_l1==1:
            print("El número de la lotería 1 fue: ", winning_numbers["Loteria1"])
        else:
            print("El número de la lotería 2 fue: ", winning_numbers["Loteria2"])
    else:
        results["Nada"] += 1

    return win_amount


for drawing in range(num_drawings):
    resultados_l1 = set(random.sample(loteria1_posibilidades, k=1))
    resultados_l2 = set(random.sample(loteria2_posibilidades, k=1))

    winning_numbers = {"Loteria1": resultados_l1, "Loteria2": resultados_l2}

    for ticket in range(tickets_per_drawing):
        total_spent += 5000
        mis_numeros = set(random.sample(loteria1_posibilidades, k=5))
        earnings += calc_win_amt(mis_numeros,winning_numbers)



print("___________________________________________________", "\n")
print(f"Total gastado: ${total_spent:,}")
print(f"Total ganado: ${earnings:,}")
print(f"Número de tiquetes comprados: {(tickets_per_drawing*num_drawings):,}")
print(json.dumps(results, indent=2))