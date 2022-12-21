with open('input.txt') as f:
    lines = f.readlines()

res = 0
win = 6
draw = 3
lose = 0
rock = 1
paper = 2
scissors = 3

for line in lines:
    print(line[0], line[2])
    if line[0] == 'A' and line[2] == 'Y':
        res += paper + win
    if line[0] == 'A' and line[2] == 'X':
        res += rock + draw
    if line[0] == 'A' and line[2] == 'Z':
        res += scissors + lose
    if line[0] == 'B' and line[2] == 'Y':
        res += paper + draw
    if line[0] == 'B' and line[2] == 'X':
        res += rock + lose
    if line[0] == 'B' and line[2] == 'Z':
        res += scissors + win
    if line[0] == 'C' and line[2] == 'Y':
        res += paper + lose
    if line[0] == 'C' and line[2] == 'X':
        res += rock + win
    if line[0] == 'C' and line[2] == 'Z':
        res += scissors + draw

print(res)