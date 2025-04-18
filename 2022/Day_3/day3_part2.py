scores = {
    'a' : 1,'b' : 2,'c' : 3,'d' : 4, 'e' : 5,'f' : 6,'g' : 7,'h' : 8,'i' : 9,'j' : 10,
    'k' : 11,'l' : 12,'m' : 13,'n' : 14,'o' : 15,'p' : 16,'q' : 17,'r' : 18,'s' : 19,
    't' : 20,'u' : 21,'v' : 22,'w' : 23,'x' : 24,'y' : 25,'z' : 26,'A' : 27,'B' : 28,
    'C' : 29,'D' : 30,'E' : 31,'F' : 32,'G' : 33,'H' : 34,'I' : 35,'J' : 36,'K' : 37,
    'L' : 38,'M' : 39,'N' : 40,'O' : 41,'P' : 42,'Q' : 43,'R' : 44,'S' : 45,'T' : 46,
    'U' : 47,'V' : 48,'W' : 49,'X' : 50,'Y' : 51,'Z' : 52
}

def compare_rucksacks(line1, line2, line3):
    return compare_first_two_rucksacks(line1.rstrip(), line2.rstrip(), line3.rstrip())


def compare_first_two_rucksacks(line1, line2, line3):
    total = 0
    for ch in line1:
        if total >= 1:
            break
        for cha in line2: 
            if line2.count(ch) >= 1:
                total = compare_third_rucksack(ch, line3)
                if total >= 1:
                    break
                break
    return total

def compare_third_rucksack(ch, line):
    print(line)
    total = 0
    if line.count(ch)>=1:
        print(ch)
        total+=scores.get(ch)
    return total

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()
    
    length = len(lines)
    loops = length//3
    total = 0
    i, j, z = 0, 1, 2
    for loop in range(loops):
        total += compare_rucksacks(lines[i], lines[j], lines[z])
        i+=3
        j+=3
        z+=3
    print(total)

