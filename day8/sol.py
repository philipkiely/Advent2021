def parse(data):
    return [t.split(" | ")[1].split() for t in data]

def count_1478(notes):
    count = 0
    for note in notes:
        for entry in note:
            if len(entry) in [2, 3, 4, 7]:
                count += 1
    return count

def parse2(data):
    return [sorted(t.split(" | ")[0].split(), key=len) for t in data], [t.split(" | ")[1].split() for t in data]

def segment_to_int(segment):
    display = {
        "1110111": 0,
        "0010010": 1,
        "1011101": 2,
        "1011011": 3,
        "0111010": 4,
        "1101011": 5,
        "1101111": 6,
        "1010010": 7,
        "1111111": 8,
        "1111011": 9
    }
    return display[segment]

def seven_one(sevenstring, onestring):
    for char in list(sevenstring):
        if char not in onestring:
            return char
    return 0

def six_long_one(sixlongs, onestring):
    for s in sixlongs:
        if onestring[0] not in s:
            return onestring[0], onestring[1]
    return onestring[1], onestring[0]

def five_long_four(fivelongs, fourstring, onestring):
    chars = [c for c in list(fourstring) if c not in onestring]
    for s in fivelongs:
        if chars[0] not in s:
            return chars[0], chars[1]
    return chars[1], chars[0]

def fivesix_long_seven(fivesixlongs, sevenstring):
    for char in list("abcdefg"):
        inall = 0
        for s in fivesixlongs:
            if char in s:
                inall += 1
        if inall == 6 and char not in sevenstring:
            return char
    return 0

def by_elimination(decoder):
    for char in list("abcdefg"):
        if char not in decoder:
            return char
    return 0

def build_decoder(signals):
    decoder = [0 for i in range(7)]
    decoder[0] = seven_one(signals[1], signals[0]) # Top of 7
    decoder[2], decoder[5] = six_long_one(signals[6:9], signals[0])
    decoder[1], decoder[3] = five_long_four(signals[3:6], signals[2], signals[0])
    decoder[6] = fivesix_long_seven(signals[3:9], signals[1])
    decoder[4] = by_elimination(decoder)
    return decoder

def decode(value, decoder):
    decoded = ["0" for i in range(7)]
    for char in list(value):
        decoded[decoder.index(char)] = "1"
    return "".join(decoded)

if __name__=="__main__":
    f = open("test.txt", "r")
    data = f.readlines()
    f.close()
    #notes = parse(data)
    #print(count_1478(notes))
    signals, values = parse2(data)
    s = 0
    for i in range(len(signals)):
        decoder = build_decoder(signals[i])
        val = ""
        for v in values[i]:
            decoded = decode(v, decoder)
            val += str(segment_to_int(decoded))
        s += int(val)
    print(s)
