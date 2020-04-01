
# Construct a list of Fibonacci series
list = []
# Your code below
limit = 20
list.append(0)
list.append(1)
for k in range(1,limit):
    n1 = list[k] + list[k-1]
    list.append(n1)
list = [x for x in list if x < limit for y in range(1, limit) if y is]
print(list)
