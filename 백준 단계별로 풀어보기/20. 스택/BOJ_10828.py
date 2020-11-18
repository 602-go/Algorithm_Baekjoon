from collections import deque
import sys

n = int(sys.stdin.readline())
stack = deque([])
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        stack.append(order[1])
    if order[0] == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    if order[0] == "size":
        print(len(stack))
    if order[0] == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    if order[0] == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])