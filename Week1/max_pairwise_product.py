# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

v1 = 0
v2 = -1

for x in a:
    if x > v1:
        v2 = v1
        v1 = x

    elif x > v2:
        v2 = x

result = v1*v2
print(result)
