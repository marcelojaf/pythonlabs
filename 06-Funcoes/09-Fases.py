n, k = int(input()), int(input())
r = []
for _ in range(n):
    r.append(int(input()))
r.sort(reverse=True)
s = k
# print(r)
for i in range(k, len(r)):
    # print(i, r[i], k, r[k])
    if (r[k-1] == r[i]):
        s += 1
print(s)
