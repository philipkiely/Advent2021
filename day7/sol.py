def parse(data):
    return [int(d) for d in data.split(",")]

def fuel_cost(pos, crabs):
    fuel = 0
    for c in crabs:
        fuel += abs(c - pos)
    return fuel

def progressive_fuel_cost(pos, crabs):
    fuel = 0
    for c in crabs:
        fuel += sum(range(1, abs(c - pos)+1))
    return fuel

def align_crabs(crabs):
    mc = min(crabs)
    xc = max(crabs)
    min_fuel = progressive_fuel_cost(mc, crabs)
    target = mc
    for i in range(mc, xc+1):
        fc = progressive_fuel_cost(i, crabs)
        if fc < min_fuel:
            min_fuel = fc
            target = i
    return target, min_fuel

if __name__=="__main__":
    f = open("test.txt", "r")
    data = f.read()
    f.close()
    crabs = parse(data)
    position, cost = align_crabs(crabs)
    print("Target:", position)
    print("Cost:", cost)
