import re

with open('input.txt') as f:
    lines = f.readlines()

fully_contained_count = 0
start1 = 0
start2 = 0
end1 = 0
end2 = 0
for line in lines:
    line = line.strip()
    line = re.split('-|,', line)
    print(line)
    start1 = int(line[0])
    end1 = int(line[1])
    start2 = int(line[2])
    end2 = int(line[3])
    if (start1>=start2 and end1<=end2) or (start2>=start1 and end2<=end1):
        fully_contained_count+=1
        print(fully_contained_count)

print(fully_contained_count)