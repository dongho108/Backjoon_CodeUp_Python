map = [list(map(int, input().split())) for i in range(10)]
x = 1
y = 1
while map[x][y] != 2:
    map[x][y] = 9
    if map[x][y+1] == 1:
        if map[x+1][y] == 1:
            break
        x = x+1
    else:
        y = y+1

if map[x][y] == 2:
    map[x][y] = 9

for i in range(10):
    for j in range(10):
        print(map[i][j], end=" ")
    print()
