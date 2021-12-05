def parse_input(data):
    vents = []
    for d in data:
        points = d.split(" -> ")
        points = [x.split(",") for x in points]
        points = [[int(x[0]), int(x[1])] for x in points]
        vents.append(points)
    return vents

def make_map(vents):
    xmax = 0
    ymax = 0
    for v in vents:
        for point in v:
            if point[0] > xmax:
                xmax = point[0]
            if point[1] > ymax:
                ymax = point[1]
    xmax += 1
    ymax += 1
    ventmap = [0 for v in range(xmax * ymax)]
    return xmax, ymax, ventmap

def print_map(xmax, ventmap):
    for i in range(int(len(ventmap)/xmax)):
        s = ""
        for x in range(xmax):
            s += str(ventmap[i*xmax+x])
        print(s)
    print("")

def is_v(vent):
    return vent[0][0] == vent[1][0]

def is_h(vent):
    return vent[0][1] == vent[1][1]

def mark_vents(xmax, ventmap, vents):
    for v in vents:
        if is_v(v):
            for i in range(v[0][1], v[1][1], 1 if v[0][1] < v[1][1] else -1):
                ventmap[(i*xmax)+v[0][0]] += 1
            ventmap[(v[1][1]*xmax)+v[0][0]] += 1 # range excludes last
        elif is_h(v):
            for i in range(v[0][0], v[1][0], 1 if v[0][0] < v[1][0] else -1):
                ventmap[(v[0][1]*xmax)+i] += 1
            ventmap[(v[0][1]*xmax)+v[1][0]] += 1  # range excludes last
    danger = 0
    for point in ventmap:
        if point >= 2:
            danger += 1
    #print_map(xmax, ventmap)
    print(danger)
    return

# Refactor of above with dx/dy variables avoids extra ventmap assignment line to compensate for range exclusion
def mark_all_vents(xmax, ventmap, vents):
    for v in vents:
        if is_v(v):
            dy = 1 if v[0][1] < v[1][1] else -1
            for i in range(v[0][1], v[1][1]+dy, dy):
                ventmap[(i*xmax)+v[0][0]] += 1
        elif is_h(v):
            dx = 1 if v[0][0] < v[1][0] else -1
            for i in range(v[0][0], v[1][0]+dx, dx):
                ventmap[(v[0][1]*xmax)+i] += 1
        else:
            dx = 1 if v[0][0] < v[1][0] else -1
            dy = 1 if v[0][1] < v[1][1] else -1
            xs = range(v[0][0], v[1][0]+dx, dx)
            ys = range(v[0][1], v[1][1]+dy, dy)
            for i in range(len(xs)):
                ventmap[xs[i]+ys[i]*xmax] += 1
    danger = 0
    for point in ventmap:
        if point >= 2:
            danger += 1
    #print_map(xmax, ventmap)
    print(danger)
    return

if __name__=="__main__":
    f = open("p1.txt", "r")
    data = f.readlines()
    f.close()
    vents = parse_input(data)
    xmax, ymax, ventmap = make_map(vents)
    mark_all_vents(xmax, ventmap, vents)
