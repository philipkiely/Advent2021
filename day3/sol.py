### HELPERS ###

def to_dec(bin, val=0):
    if len(bin) == 0:
        return val
    return to_dec(bin[1:], val+(int(bin[0])*2**(len(bin)-1)))

#print(to_dec("0")) # 0
#print(to_dec("1"))  # 1
#print(to_dec("10110")) # 22
#print(to_dec("01001")) # 9

### SOL ###

f = open("p1.txt", "r")
bits = f.readlines()
f.close()

gamma = ""
epsilon = ""

for i in range(0, len(bits[0])-1):
    zeros = 0
    ones = 0
    for b in bits:
        if b[i] == "1":
            ones += 1
        else: # b[i] == "0"
            zeros += 1
    if ones > zeros:
        gamma += "1"
        epsilon += "0"
    else: # zeros < ones
        gamma += "0"
        epsilon += "1"
    # Problem does not specify what to do if equal

print("gamma:", gamma, "=", to_dec(gamma))
print("epsilon:", epsilon, "=", to_dec(epsilon))
print("answer:", to_dec(gamma)*to_dec(epsilon))
print("\n\n")

bits = [b.strip("\n") for b in bits]

oxygen = bits.copy()
co2 = bits.copy()

for i in range(0, len(bits[0])):
    zeros = []
    ones = []
    if len(oxygen)> 1:
        for b in oxygen:
            if b[i] == "1":
                ones.append(b)
            else:  # b[i] == "0"
                zeros.append(b)
        if len(ones) >= len(zeros):
            oxygen = ones.copy()
        else:  # len(ones) < len(zeros)
            oxygen = zeros.copy()
    zeros = []
    ones = []
    if len(co2) > 1:
        for b in co2:
            if b[i] == "1":
                ones.append(b)
            else:  # b[i] == "0"
                zeros.append(b)
        if len(zeros) <= len(ones):
            co2 = zeros.copy()
        else:  # len(zeros) > len(ones)
            co2 = ones.copy()

print("oxygen:", oxygen[0], "=", to_dec(oxygen[0]))
print("co2:", co2[0], "=", to_dec(co2[0]))
print("answer:", to_dec(oxygen[0])*to_dec(co2[0]))
