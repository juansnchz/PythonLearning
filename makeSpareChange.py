def makeChange(cents):
    coins = {}
    if cents // 25 > 0:
        coins["quarters"] = cents // 25
        cents = cents % 25
    if cents // 10 > 0:
        coins["dimes"] = cents // 10
        cents = cents % 10
    if cents // 5 > 0:
        coins["nickels"] = cents // 5
        cents = cents % 5
    if cents > 0:
        coins["pennies"] = cents
    return coins


assert makeChange(30) == {'quarters': 1, 'nickels': 1}
assert makeChange(10) == {'dimes': 1}
assert makeChange(57) == {'quarters': 2, 'nickels': 1, 'pennies': 2}
assert makeChange(100) == {'quarters': 4}
assert makeChange(125) == {'quarters': 5}
