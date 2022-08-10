# 고정 길이 스택 클래스(FixedStack) 사용 

from fixed_stack import FixedStack
from enum import Enum

Menu = Enum("Menu", ["push","pop","peek","find","dump","cancle"])

# 메뉴 선택 
def select_menu():
    s = [f"({m.value}){m.name}" for m in Menu]

    while True:
        print(*s, sep="     ", end="")

        n = int(input(" : "))
        if n >= 1 and n <= len(Menu):
            return Menu(n)

s = FixedStack(64)  # 최대 64개를 push할 수 있는 Stack

while True :
    print(f"Current data : {len(s)} / {s.capacity}")
    m = select_menu()    # 메뉴 선택

    if m == Menu.push :  # push
        x = int(input("push data : "))
        try :
            s.push(x)
        except FixedStack.Full:
            print("Stack is Full")
    
    elif m == Menu.pop:  # pop
        try :
            x = s.pop()
            print(f"pop data : {x}")
        except FixedStack.Empty:
            print("Stack is Empty")
    
    elif m == Menu.peek: # peek
        try :
            x = s.peek()
            print(f"peek data : {x}")
        except FixedStack.Empty:
            print("Stack is Empty")
    
    elif m == Menu.find: # find
        x = int(input("find data : "))

        if x in s :
            print(f"count : {s.count(x)}, index : {s.find(x)}")
        else :
            print("No data")
    
    elif m == Menu.dump: # dump
        s.dump()
    
    else :               # cancle
        print("End")
        break 
