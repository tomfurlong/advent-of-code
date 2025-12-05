with open('input_example.txt') as f:
    lines = f.readlines()

safe_count=0
for line in lines:
    list_0=[]
    list_0.append(line.split())
    length = len(list_0)
    print(type(list_0))
    i=0
    list_0 = list(map(int, list_0))

    print(list_0)
    # while i<length-1:
        
    #     if(abs(list_0[i]-list_0)