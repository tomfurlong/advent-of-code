with open('input.txt') as f:
    lines = f.readlines()

for line in lines: 
    line = line.rstrip()
    if(line[0].isdigit()):
        print(line)