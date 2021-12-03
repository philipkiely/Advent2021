f = open("p1.txt", "r")
dxn = [[x[0], int(x[1])] for x in [l.split(" ") for l in f.readlines()]]
f.close()

pos = 0
dep = 0

for d in dxn:
    if d[0] == "forward":
        pos += d[1]
    elif d[0] == "up":
        dep -= d[1]
    else: # d[0] == "down"
        dep += d[1]

print("pos", pos)
print("dep", dep)
print("ans", pos*dep)
print("\n\n")

pos = 0
dep = 0
aim = 0

for d in dxn:
    if d[0] == "forward":
        pos += d[1]
        dep += aim*d[1]
    elif d[0] == "up":
        aim -= d[1]
    else:  # d[0] == "down"
        aim += d[1]

print("pos", pos)
print("dep", dep)
print("aim", aim)
print("ans", pos*dep)
