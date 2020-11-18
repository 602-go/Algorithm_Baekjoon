from collections import deque
n, k = map(int, input().split())
queue = deque([])
for i in range(1,n+1):
    queue.append(i)
print("<", end="")
while queue:
    for i in range(k-1): #i=0,1
        queue.append(queue[0]) #[1,2,,,,,,,7,1]
        queue.popleft() #[3,4,5,6,7,1,2]
    print(queue.popleft(), end="") #[4,5,6,7,1,2] #[7,1,2,4,5] #[4,5,7,1]
    if queue:
        print(",", end=" ")
print(">")