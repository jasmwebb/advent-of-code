def calc_fuel(mass):
    fuel = int(mass) // 3 - 2
    
    if fuel < 0:
        return 0
    
    return fuel + calc_fuel(fuel)
    

with open("input.txt", "r") as inputf:
    fuel_needed = (calc_fuel(mass) for mass in inputf)
    print(sum(fuel_needed))
