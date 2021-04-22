n  = int(input())

person = list(map(int, input().split()))

person.sort()

acc = [person[0]]

for i in range(1, len(person)):
    
    acc.append(acc[-1] + person[i])


print(sum(acc))