with open('input.txt') as f:
    lines = f.readlines()

start_of_packet=0
end_of_packet=14
lines = str(lines).strip('[|\'|]')
print(lines)
substring = lines[start_of_packet:end_of_packet]
for ch in lines:
    substring = lines[start_of_packet:end_of_packet]
    print(substring)
    print(set(substring))
    if len(substring) < 14:
        break

    ans = set(substring)
    if len(ans)==14:
        print(ans)
        print(end_of_packet)
        break

    start_of_packet+=1
    end_of_packet+=1