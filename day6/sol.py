def parse(data):
    fish = [int(n) for n in data.split(",")]
    school = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    for i in fish:
        school[i] += 1
    return school

def day(school):
    new_school = {}
    new_school[8] = school[0]
    new_school[7] = school[8]
    new_school[6] = school[7] + school[0]
    for i in range(5, -1, -1):
        new_school[i] = school[i+1]
    return new_school

def count_fish(school):
    count = 0
    for key in school:
        count += school[key]
    return count

if __name__=="__main__":
    f = open("test.txt", "r")
    data = f.read()
    f.close()
    school = parse(data)
    for i in range(256):
        school = day(school)
    print(count_fish(school))