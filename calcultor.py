def add(n1,n2):
    n3 = n1+n2
    return n3

def sub(n1,n2):
    n3 = n1-n2
    return n3

def mul(n1,n2):
    n3 = n1*n2
    return n3

def div(n1,n2):
    n3 = n1/n2
    return n3

def squ(n1,n2):
    n2 = n1**n2
    return n2

def rem(n1,n2):
    n3 = n1%n2
    return n3

operations= {"+":add, "-": sub, "/": div, "*": mul, "**": squ, "%": rem}

def calculator():
    n1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    should_cont = True
    while should_cont:
        op = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        n3 = operations[op](n1,n2)

        print(f"{n1} {op} {n2} = {n3}")
        con = input(f"Type 'y' to continue calculating with {n3}, or type 'n' to start a new calculation: ")
        if con=="y":
            n1 = n3
        else:
            should_cont = False
            calculator()

calculator()
