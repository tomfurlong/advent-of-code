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
similarity_score = 0
total_similarity_score = 0
while  i <= length-1:
    print((list_1[i]), list_2)
    if list_2.count(list_1[i]):
        similarity_score = int(list_1[i]) * list_2.count(list_1[i])
        total_similarity_score += similarity_score
    i+=1

print(total_similarity_score)