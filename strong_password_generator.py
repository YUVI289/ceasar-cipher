import string
import random

complete_list = list(string.printable)+list(string.ascii_letters)+list(str(range(0,10)))
password=[]
for i in range(0,9):
    password.append(random.choice(complete_list))
passy = ""
for i in password:
    passy+=i
print(passy)