hours = ["12","1","2","3","4","5","6","7","8","9","10","11"]
minutes = ["00","15","30","45"]
daytimes = ["am", "pm"]

for daytime in daytimes:
    for hour in hours:
        for minute in minutes:
            print(f"{hour}:{minute} {daytime}")