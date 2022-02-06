import string
import random

print("Welcome to the PyPassword Generator!")
no_of_letters=int(input("How many letters would you like in your password?\n"))
no_of_symbols=int(input("How many symbols would you like?\n"))
no_of_numbers=int(input("How many numbers would you like?\n"))

alphabets = list(string.ascii_letters)
numbers= list(range(0,10))
symbols=list(string.punctuation)

password = []
for i in range(0,no_of_letters+1):
    password.append(random.choice(alphabets))

for i in range(0,no_of_symbols+1):
    password+=(random.choice(symbols))

for i in range(0,no_of_numbers+1):
    password+=str(random.choice(numbers))
    

random.shuffle(password)
gp=""
for i in password:
    gp+=i

print(f"Here is your password: {gp}")
