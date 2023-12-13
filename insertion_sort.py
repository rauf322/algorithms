a = [100,4,0,5,3,2,1]

for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)