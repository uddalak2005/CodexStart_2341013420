#Name: Uddalak Mukhopadhyay
#Registration Number: 2341013420
#Problem link: https://cses.fi/problemset/task/1755



st=input()
dic={}

for i in range(26):
    dic[chr(i+ord('A'))]=0
for i in st:
    dic[i]+=1

odd_counter=0
for i in dic:
    if dic[i]%2!=0:
        odd_counter+=1

if odd_counter>1:
    print("NO SOLUTION")
else:
    pal=""
    for i in dic:
        if dic[i]%2!=0:
            pal=i*dic[i]
            dic[i]=0
            break
    for i in dic:
        if dic[i]>0:
            pal=(i*(dic[i]//2))+pal+(i*(dic[i]//2))
            dic[i]=0
    print(pal)