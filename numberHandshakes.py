def printHandshakes(people:list):
    numberHandshakes = 0
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            print(f"{people[i]} shakes hands with {people[j]}")
            numberHandshakes +=1
    print(f"There were a total of {numberHandshakes} handshakes.")
    return numberHandshakes


printHandshakes(['Alice', 'Bob', 'Carol', 'David', "Yurani", "Paquita", "Feliciana", "Papina", "Gatinski"])

