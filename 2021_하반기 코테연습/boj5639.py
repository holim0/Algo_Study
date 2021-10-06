import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
number = []


            



def postOrder(s, e):
   
    if s>e:
        return 
    else:
        root = number[s]
        divide = e+1
        for i in range(s+1, e+1):
            if number[i]>root:
                divide = i
                break
        postOrder(s+1, divide-1)
        postOrder(divide, e)
        print(root)


while 1:
  try:
    number.append(int(input()))
  except:
    break

start, end = 0, len(number)-1
postOrder(start, end)

