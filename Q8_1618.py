#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/1618


n=int(input())
power=5
count=0
while(n>=power):
    count+=n//power
    power*=5
print(count)