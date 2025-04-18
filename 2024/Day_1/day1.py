with open('input.txt') as f:
    lines = f.readlines()

list_1 = []
list_2 = []
list_0 = []
for line in lines:
    list_0 = line.split()
    list_1.append(list_0[0])
    list_2.append(list_0[-1])

list_1.sort()
list_2.sort()

length = len(list_1)

i = 0
total_distance = 0
while  i <= length-1:
    distance_between = abs(int(list_1[i]) - int(list_2[i]))
    total_distance += distance_between
    i+=1

print(total_distance)