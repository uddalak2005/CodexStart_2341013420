#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/1071


n=int(input())
if n==1:
    print('1')
elif n<=3:
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i,end=" ")
    for i in range(1,n+1,2):
        print(i,end=" ")
    