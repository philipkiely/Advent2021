def parse(data):
    return len(data.split("\n")[0]), [int(d) for d in list(data) if d != "\n"]

def pretty_print(xlen, heights):
    for row in range(int(len(heights)/xlen)):
        s = ""
        for i in range(xlen):
            s += str(heights[row*xlen+i])
        print(s)
    print("")

def risk_levels(xlen, heights):
    risk = 0
    hlen = len(heights)
    for i in range(hlen):
        # Literally edge and corner cases, not funny
        if i == 0: # Top left corner
            if all(heights[i] < x for x in [heights[i+1], heights[i+xlen]]):
                risk += (1 + heights[i])
        elif i == xlen-1: # Top right corner
            if all(heights[i] < x for x in [heights[i-1], heights[i+xlen]]):
                risk += (1 + heights[i])
        elif i == hlen-xlen: # Bottom left corner
            if all(heights[i] < x for x in [heights[i+1], heights[i-xlen]]):
                risk += (1 + heights[i])
        elif i == hlen-1: # Bottom right corner
            if all(heights[i] < x for x in [heights[i-1], heights[i-xlen]]):
                risk += (1 + heights[i])
        elif i < xlen: # Top Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i+xlen]]):
                risk += (1 + heights[i])
        elif i % xlen == 0: # Left Edge
            if all(heights[i] < x for x in [heights[i+1], heights[i-xlen], heights[i+xlen]]):
                risk += (1 + heights[i])
        elif (i+1) % xlen == 0: # Right Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i-xlen], heights[i+xlen]]):
                risk += (1 + heights[i])
        elif i > (hlen-xlen): # Bottom Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i-xlen]]):
                risk += (1 + heights[i])
        else: # Middle
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i-xlen], heights[i+xlen]]):
                risk += (1 + heights[i])
    return risk

#################################
# PART 2 ATTEMPT (Doesn't Work) #
#################################

def nine_up(i, xlen, heights, s=0):
    j = 1
    if((i - (j*xlen)) > 0 and heights[i - (j*xlen)] < 9):
        heights[i - (j*xlen)] = 9
        l, heights = nine_left(i - (j*xlen), xlen, heights)
        r, heights = nine_right(i - (j*xlen), xlen, heights)
        s += 1 + l + r
        s, heights = nine_up(i - (j*xlen), xlen, heights, s)
        j += 1
    return s, heights

def nine_left(i, xlen, heights, s=0):
    j = 1
    if((i - j) % xlen > 0 and heights[i - j] < 9):
        heights[i - j] = 9
        u, heights = nine_up(i - j, xlen, heights)
        d, heights = nine_down(i - j, xlen, heights)
        s += 1 + u + d
        s, heights = nine_left(i - j, xlen, heights, s)
        j += 1
    return j-1, heights

def nine_right(i, xlen, heights, s=0):
    j = 1
    if((i + j) % xlen > 0 and heights[i + j] < 9):
        heights[i + j] = 9
        u, heights = nine_up(i + j, xlen, heights)
        d, heights = nine_down(i + j, xlen, heights)
        s += 1 + u + d
        s, heights = nine_right(i + j, xlen, heights, s)
        j += 1
    return j-1, heights

def nine_down(i, xlen, heights, s=0):
    j = 1
    if((i + (j*xlen)) < len(heights) and heights[i + (j*xlen)] < 9):
        heights[i - (j*xlen)] = 9
        l, heights = nine_left(i - (j*xlen), xlen, heights)
        r, heights = nine_right(i - (j*xlen), xlen, heights)
        s += 1 + l + r
        s, heights = nine_down(i + (j*xlen), xlen, heights, s)
        j += 1
    return s, heights

def basins(xlen, heights):
    basins = []
    hlen = len(heights)
    for i in range(hlen):
        basin_size = 1
        # Literally edge and corner cases, not funny
        if i == 0:  # Top left corner
            if all(heights[i] < x for x in [heights[i+1], heights[i+xlen]]):
                pass
        elif i == xlen-1:  # Top right corner
            if all(heights[i] < x for x in [heights[i-1], heights[i+xlen]]):
                pass
        elif i == hlen-xlen:  # Bottom left corner
            if all(heights[i] < x for x in [heights[i+1], heights[i-xlen]]):
                pass
        elif i == hlen-1:  # Bottom right corner
            if all(heights[i] < x for x in [heights[i-1], heights[i-xlen]]):
                pass
        elif i < xlen:  # Top Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i+xlen]]):
                pass
        elif i % xlen == 0:  # Left Edge
            if all(heights[i] < x for x in [heights[i+1], heights[i-xlen], heights[i+xlen]]):
                pass
        elif (i+1) % xlen == 0:  # Right Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i-xlen], heights[i+xlen]]):
                pass
        elif i > (hlen-xlen):  # Bottom Edge
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i-xlen]]):
                pass
        else:  # Middle
            if all(heights[i] < x for x in [heights[i-1], heights[i+1], heights[i-xlen], heights[i+xlen]]):
                print(i)
                pretty_print(xlen, heights)
                heights[i] = 9
                up, heights = nine_up(i, xlen, heights)
                print(up)
                print("")
                pretty_print(xlen, heights)
                left, heights = nine_left(i, xlen, heights)
                print("")
                pretty_print(xlen, heights)
                right, heights = nine_right(i, xlen, heights)
                print("")
                pretty_print(xlen, heights)
                down, heights = nine_down(i, xlen, heights)
                print("")
                pretty_print(xlen, heights)
                basin_size += up + left + right + down
                basins.append(basin_size)
    return basins

####################
# PART 2 ATTEMPT 2 #
####################



if __name__=="__main__":
    f = open("train.txt", "r")
    data = f.read()
    f.close()
    xlen, heights = parse(data)
    print(risk_levels(xlen, heights))
    #print(basins(xlen, heights))
