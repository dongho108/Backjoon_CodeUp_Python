num = list(map(int, input().split()))
i = 1
result = num[0];
while i < num[2]:
    result = result * num[1]
    i = i+1
print(result)
