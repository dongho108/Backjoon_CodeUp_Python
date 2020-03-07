import sys
input = sys.stdin.readline


class Stack:
    def __init__(self):
        self.stack = []
        self._size = 0
    def push(self, input):
        self.stack.append(input)
        self._size = self._size + 1
    def pop(self):
        if not self.stack:
            return -1
        else:
            self.temp = self.stack[-1]
            self.stack.pop()
            self._size = self._size - 1
            return self.temp
    def size(self):
        return self._size
    def empty(self):
        if not self.stack:
            return 1
        else:
            return 0
    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[self._size-1]

num = int(input())
st = Stack()
for i in range(0,num):
    in_put = input().strip().split()
    if in_put[0] == "push":
        st.push(int(in_put[1]))
    elif in_put[0] == "pop":
        print(st.pop())
    elif in_put[0] == "size":
        print(st.size())
    elif in_put[0] == "empty":
        print(st.empty())
    elif in_put[0] == "top":
        print(st.top())
