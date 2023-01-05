import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

print(lines)
matrix = []
array = np.array([])
total = len(lines) * len(lines[0].rstrip())
shape = (len(lines),len(lines[0].rstrip()))
non_vis = 0

for line in lines:
    line = line.rstrip()
    array1 = []
    for tree in line:
        array1 = np.asarray(np.append(array1, int(tree)))
    array = np.append(array, array1, axis=0)

array = array.reshape(shape)
print(array)
# print(array[:,1])
x,y = 1, 1

end_x = len(lines) - 1
end_y = len(lines[0].rstrip()) - 1
inside_count = 0 
for i in range(1, 4):
    for j in range(1, 4):
        tree = array[i][j]
        pos = [i, j]
        col = array[:,i]
        print(col)
        top = np.split(col, [i,5])[0]
        bottom = np.split(col, [i,2,5])[2]
        print(top, bottom)
        top_max = np.max(top)
        bottom_max = np.max(bottom)
        if (tree > top_max or tree > bottom_max) :
            print("visible")
            inside_count+=1
            continue
        

        print(array[j])
        print("------------")

print(inside_count)

# if the tree is the smallest in the row or the column 
# then the no visible count should be incremented and
# we subtract this from the total to find the total 
# no of visible trees
