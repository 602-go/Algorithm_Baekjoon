from collections import deque
import sys


n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    x = sys.stdin.readline().split()
    if x[0] == "push_front":
        queue.appendleft(x[1])
    elif x[0] == "push_back":
        queue.append(x[1])
    elif x[0] == "pop_front":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif x[0] == "pop_back":
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif x[0] == "size":
        print(len(queue))
    elif x[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif x[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif x[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])