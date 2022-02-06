num_limit=int(input("How many numbers? "))
a,b=0,1
series_list=[]
for i in range(0,num_limit):
    c=a+b
    a=b
    b=c
    series_list.append(str(a))
print(series_list)

n1=""
n2=[]
for n in range(0,len(series_list)):
    n1=(str(n1)+series_list[n]) 
    n2.append(n1)
print(n2)

n3=0
for n in range(0,len(series_list)):
    n3=n3+int(n2[n])

print(f"{n3}\n{n3%10}")