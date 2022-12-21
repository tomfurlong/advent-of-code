largest = 0
next = 0
with open('input.txt') as f:
    lines = f.readlines()

group_count = 1
for line in lines:
    if line == '\n':
        group_count+=1

for line in lines:
    if line == '\n':
        print(next)
        if next>largest:
            print('New largest: ', next, ' Prev largest: ', largest)
            largest = next
        next = 0
        continue 
    next += int(line)
    print('largest: ' ,largest, ' next: ', next)
    
    
print(largest)