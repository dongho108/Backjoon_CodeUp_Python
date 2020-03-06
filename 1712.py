A, B, C = map(int, input().split())
if B >= C:
    print(int(-1))
else:
    print((A//(C-B))+1)
