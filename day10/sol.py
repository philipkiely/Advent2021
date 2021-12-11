def score(char):
    scores = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    return scores[char]

def matches(popped, char):
    pairs = {
        "{": "}",
        "[": "]",
        "<": ">",
        "(": ")"
    }
    return pairs[popped] == char

def inquiry(line):
    stack = []
    for char in list(line):
        if char in ["<", "[", "{", "("]:
            stack.append(char)
        else:
            if not matches(stack.pop(), char):
                return score(char)
    return 0

def repair(line):
    stack = []
    for char in list(line):
        if char in ["<", "[", "{", "("]:
            stack.append(char)
        else:
            stack.pop() # Garanteed to match because we already checked for corruption
    points = {
        "{": 3,
        "[": 2,
        "<": 4,
        "(": 1
    }
    skor = 0
    stack.reverse()
    for c in stack:
        skor *= 5
        skor += points[c]
    return skor    

if __name__=="__main__":
    f = open("test.txt", "r")
    data = [l.strip() for l in f.readlines()]
    f.close()
    s = 0
    for line in data:
        s += inquiry(line)
    print(s)
    s2 = []
    for line in data:
        if inquiry(line) == 0:
            s2.append(repair(line))
    s2 = sorted(s2)
    print(s2[int(len(s2)/2)])
