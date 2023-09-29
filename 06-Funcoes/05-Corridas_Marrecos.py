num = int(input())
while num > 0:
    num_corridas = 0
    while num > 1:
        if num % 3 == 0:
            num = num / 3
        else:
            num = (num // 3) + 1
        num_corridas = num_corridas + num
    print(int(num_corridas))
    num = int(input())
