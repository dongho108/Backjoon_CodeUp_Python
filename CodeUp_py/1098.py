x, y = map(int, input().split())
num = int(input())
data = [list(map(int, input().split())) for i in range(num)]
map = [[0]*(y+1) for i in range(x+1)]
for i in range(num):
    xx = data[i][2]
    yy = data[i][3]
    for j in range(data[i][0]):
        map[xx][yy] = 1
        if data[i][1] == 0:
            yy = yy+1
        else:
            xx = xx+1
for i in range(1, x+1):
    for j in range(1, y+1):
        print(map[i][j], end=" ")
    print()
