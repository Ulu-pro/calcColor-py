from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
actions = ["+","-","*","/"]
d = Fore.BLACK+Back.YELLOW
def danger():
    print(Fore.WHITE+Back.RED+" Error. Try again ")
def r(s):
    print(Fore.YELLOW+Back.BLUE+Style.BRIGHT+" Result: "+str(s)+" ")
print(Fore.BLACK+Back.WHITE+' For exit enter "EXIT" ')
while 1:
    while 1:
        x = input(" Action(+,-,*,/): ")
        if x == "EXIT":
            exit(d+" EXIT of the Program ")
        if x in actions:
            break
        else:
            danger()
    while 1:
        try:
            a = input(" First  number: ")
            if a == "EXIT":
                exit(d+" EXIT of the Program ")
            a = float(a)
            break
        except ValueError:
            danger()
    while 1:
        try:
            b = input(" Second number: ")
            if b == "EXIT":
                exit(d+" EXIT of the Program ")
            b = float(b)
            break
        except ValueError:
            danger()
    if x == "+":
        r(a+b)
    elif x == "-":
        r(a-b)
    elif x == "*":
        r(a*b)
    elif x == "/":
        r(a/b)
    print('-'*20)