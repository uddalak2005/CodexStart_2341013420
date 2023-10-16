#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/1092



n=int(input())

if n%4==1 or n%4==2:
    print("NO")

else:
    print("YES")
    if n%4==0:
        print(n//2)
        for i in range(1,n+1,4):
            print(i,i+3,end=" ")
        print()
        print(n//2)
        for i in range(1,n+1,4):
            print(i+1,i+2,end=" ")
    else:
        print(n//2+1)
        print("1 2",end=" ")
        for i in range(4,n+1,4):
            print(i,i+3,end=" ")
        print()
        print(n//2)
        print("3",end=" ")
        for i in range(4,n+1,4):
            print(i+1,i+2,end=" ")
