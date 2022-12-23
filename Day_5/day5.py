with open('input.txt') as f:
    lines = f.readlines()

crates = []
for line in lines:
    if line == '\n':
        break
    # line = line.strip()
    # crates = crates.vstack([crates, line])
    print(line)
    crates.append(line)
    


for l in crates:
    print(l)