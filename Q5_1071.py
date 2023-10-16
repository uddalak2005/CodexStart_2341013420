#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/1071


n=int(input())
for _ in range(n):
    r,c=map(int, input().split())
    if r>c:
        if r%2==0:
            print(r**2-(c-1))
        else:
            print((r-1)**2+1+(c-1))
    else:
        if c%2==0:
            print((c-1)**2 + 1 + (r-1))
        else:
            print(c**2 - (r-1))