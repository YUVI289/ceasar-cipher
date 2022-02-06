num_limit=int(input("How many numbers? "))
a,b=0,1
series_list=[]
for i in range(0,num_limit):
    c=a+b
    a=b
    b=c
    series_list.append(str(a))
print(series_list)
