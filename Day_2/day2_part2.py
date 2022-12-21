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
    if line[0] == 'A' and line[2] == 'Y':
        res += rock + draw
    if line[0] == 'A' and line[2] == 'X':
        res += scissors + lose
    if line[0] == 'A' and line[2] == 'Z':
        res += paper + win
    if line[0] == 'B' and line[2] == 'Y':
        res += paper + draw
    if line[0] == 'B' and line[2] == 'X':
        res += rock + lose
    if line[0] == 'B' and line[2] == 'Z':
        res += scissors + win
    if line[0] == 'C' and line[2] == 'Y':
        res += scissors + draw
    if line[0] == 'C' and line[2] == 'X':
        res += paper + lose
    if line[0] == 'C' and line[2] == 'Z':
        res += rock + win

print(res)