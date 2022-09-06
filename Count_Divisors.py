n,r,l=map(int,input().split())
count=0
for i in range(n,r+1,1):
    if (i%l==0):
        count+=1
print(count)