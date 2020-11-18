from collections import deque

t = int(input())
for _ in range(t):
    order = input()
    n = int(input())
    que = input()
    que = que.strip("]")
    que = que.strip("[")
    if n == 0:
        deq = deque([])
    else:
        deq =deque(que.split(","))
    rev = 1
    p = 0
    for o in order:
        if o == "R":
            rev *= -1
        elif o == "D":
            if not deq:
                p = 1
                break
            else:
                if rev == 1:
                    deq.popleft()
                elif rev == -1:
                    deq.pop()
    if p == 1:
        print("error")
    else:
        if rev == -1:
            deq.reverse()
        print("[", ",".join(map(str, deq)), "]", sep="")