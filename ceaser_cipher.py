from re import I
import string

alphabet = list(string.ascii_lowercase + string.ascii_lowercase)

def ceaser(input1, num1):
    output1 = ""
    if direction=="decode":
        num1*= -1
    for i in input1:
        if i in alphabet:
            num2 = alphabet.index(i)
            num3 = num2+num1
            output1 += alphabet[num3]
        else:
            output1=output1+i
    print(f"The {direction}d text is {output1}")
state=True
while state:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    ceaser(input1=text, num1=shift)
    decides = input("Type'yes' if you want to go again. Otherwise type 'no'\n")
    
    if decides=="no":
        state=False
        print("Bye")