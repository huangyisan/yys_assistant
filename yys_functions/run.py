def ju(n):
    return n[0] == 0

a = [(0,'123'),(1,'222'),(0,'0')]

# a = filter(ju,a)
a = filter(lambda x:x[0]==0,a)
print(list(a))