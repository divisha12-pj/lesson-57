#sum of natural numbers
def sum(n):
    return n*(n+1)/2
print(sum(8))

#sum of list numbers
def aarsum(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    print(sum)
a=[10,20,30,40,50]
aarsum(a)

def sum(n):
    if n<=0:
        return 0
    return(n+ sum(n-1))



print(sum(8))

    