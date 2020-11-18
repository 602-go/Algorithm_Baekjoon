from collections import deque
import sys

def push(queue,x):
    queue.append(x)
    return queue
def pop(queue):
    if not queue: # len(queue) == 0
        print(-1)
    else:
        print(queue.popleft())
def size(queue):
    print(len(queue))
def empty(queue):
    if not queue:
        print(1)
    else:
        print(0)
def front(queue):
    if not queue:
        print(-1)
    else:
        print(queue[0])
def back(queue):
    if not queue:
        print(-1)
    else:
        print(queue[-1])

n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    q = sys.stdin.readline().split()
    if q[0] == "push":
        push(queue, q[1])
    elif q[0] == "pop":
        pop(queue)
    elif q[0] == "size":
        size(queue)
    elif q[0] == "empty":
        empty(queue)
    elif q[0] == "front":
        front(queue)
    elif q[0] == "back":
        back(queue)