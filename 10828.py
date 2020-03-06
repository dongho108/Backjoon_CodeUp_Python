class Stack:
    stack = []
    def push(self, input):
        Stack.stack.append(input)
    def pop(self):
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            Stack.stack.pop()
    def size(self):
        print(len(Stack.stack))
    def empty(self):
        if not stack:
            print(1)
        else:
            print(0)
    def top(self):
        if not stack:
            print(-1)
        else:
            print(stack[0])

num = 14
st = Stack()
for i in range(0,num):
    in_str, in_num = input().split()
    if in_str == "push":
        st.push(int(in_num))
    elif in_str == "pop":
        st.pop()
    elif in_str == "size":
        st.size()
    elif in_str == "empty":
        st.empty()
    elif in_str == "top":
        st.top()
