largest = 0
second_largest = 0
third_largest=0
next = 0
with open('input.txt') as f:
    lines = f.readlines()

group_count = 1
for line in lines:
    if line == '\n':
        group_count+=1

for line in lines:
    if line == '\n':
        print(next, largest, second_largest, third_largest)
        if next>largest:
            third_largest=second_largest
            second_largest=largest
            largest = next
        elif next>second_largest:
            third_largest = second_largest
            second_largest = next
        elif next>third_largest:
            third_largest = next
        next = 0
        continue 
    next += int(line)
    
    
print(largest, second_largest, third_largest)
print(largest + second_largest + third_largest)