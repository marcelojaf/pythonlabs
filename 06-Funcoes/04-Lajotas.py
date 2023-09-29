m = {0: 1, 1: 1}

while True:
    inp = input()
    if inp == "0":
        break
    for i in range(len(m), int(inp)+1):
        m[i] = m[i-1] + m[i-2]
    print(m[int(inp)])
