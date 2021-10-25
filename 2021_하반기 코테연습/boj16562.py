from collections import deque
n, m, k = map(int, input().split())

cost = list(map(int, input().split()))

parent = [i for i in range(n+1)]
cost.insert(0, -1)

def find(x):

    if x==parent[x]: return x

    p = find(parent[x])

    parent[x] = p 

    return p


def merge(x, y):

    x= find(x)
    y = find(y)

    if x==y: return

    if cost[x]<cost[y]:
        parent[y] = x
    
    else:
        parent[x] = y

    
for _ in range(m):
    a, b = map(int, input().split())
    merge(a, b)

answer = 0
for i in range(1, n+1):
    cp = find(i)
    if cp!=0:
        answer+=cost[cp]
        merge(0, cp)


# q = deque([])
# INF = 1e10

# for i in range(1, n+1):
#     min_val = INF
#     target = -1
#     if not check[i]:
#         if min_val>cost[i-1]:
#             min_val=cost[i-1]
#             target = i

#         check[i] = True
#         q.append(i)

#         while q:
#             cur = q.popleft()

#             for nxt in link[cur]:
#                 if not check[nxt]:
#                     check[nxt] = True

#                     if min_val>cost[nxt-1]:
#                         min_val = cost[nxt-1]
#                         target = nxt
                    
#                     q.append(nxt)
#         answer+=min_val


if answer<=k:
    print(answer)
else:
    print("Oh no")

