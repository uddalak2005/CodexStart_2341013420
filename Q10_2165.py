#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/2165


def towerOfHanoi(n,source,destination,auxiliary):
    if n==0:
        return
    towerOfHanoi(n-1,source,auxiliary,destination)
    print(source,destination)
    towerOfHanoi(n-1,auxiliary,destination,source)

n=int(input())
print(2**n-1)
towerOfHanoi(n,1,3,2)