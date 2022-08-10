from fixed_stack import FixedStack
from enum import Enum

Menu = Enum("Menu", ["push","pop","peek","find","dump","cancle"])

def select_menu():
    s = [f"({m.value}){m.name}" for m in Menu]

    while True:
        print(*s, sep="     ", end="")

        n = int(input(" : "))
        if n >= 1 and n <= len(Menu):
            return Menu(n)

s = FixedStack(64)

while True :
    print(f"Current data : {len(s)} / {s.capacity}")
    m = select_menu()

    if m == Menu.push :
        x = int(input("push data : "))
        try :
            s.push(x)
        except FixedStack.Full:
            print("Stack is Full")
    
    elif m == Menu.pop:
        try :
            x = s.pop()
            print(f"pop data : {x}")
        except FixedStack.Empty:
            print("Stack is Empty")
    
    elif m == Menu.peek:
        try :
            x = s.peek()
            print(f"peek data : {x}")
        except FixedStack.Empty:
            print("Stack is Empty")
    
    elif m == Menu.find:
        x = int(input("find data : "))

        if x in s :
            print(f"count : {s.count(x)}, index : {s.find(x)}")
        else :
            print("No data")
    
    elif m == Menu.dump:
        s.dump()
    
    else :
        print("End")
        break 
