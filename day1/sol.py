f = open("p1.txt", "r")
data = [int(n) for n in f.readlines()]
f.close()

c = 0
cb = 0

#for i in range(1, len(data)):
#    if data[i] > data[i-1]:
#        c += 1

for i in range(0, len(data)-2):
    cb += 1
    if sum(data[i:i+3]) < sum(data[i+1:i+4]):
        c += 1

print(c)
print(cb)