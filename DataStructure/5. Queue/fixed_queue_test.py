from enum import Enum
from fixed_queue import FixedQueue

Menu = Enum("Menu", ["enqueue", "dequeue", "peek", "find", "dump", "cancle"])

def select_menu():
    s = [f"({m.value}){m.name}" for m in Menu]
    while True :
        print(*s, sep="     ", end="")
        n = int(input(" : "))
        if n >= 1 and n <= len(Menu):
            return Menu(n)

q = FixedQueue(64)

while True :
    print(f"Current data : {len(q)} / {q.capacity}")
    m = select_menu()

    if m == Menu.enqueue :
        x = int(input("enqueue data : "))
        try :
            q.enqueue(x)
        except FixedQueue.Full:
            print("Queue is Full")
    
    elif m == Menu.dequeue :
        try :
            x =  q.dequeue()
            print(f"dequeue data : {x}")
        except FixedQueue.Empty :
            print("Queue is Empty")

    elif m == Menu.peek :
        try :
            x =  q.peek()
            print(f"peek data : {x}")
        except FixedQueue.Empty :
            print("Queue is Empty")

    elif m == Menu.find :
        x = int(input("find data : "))
        if x in q :
            print(f"count : {q.count(x)}, index : {q.find(x)}")
        else :
            print("No data")
    
    elif m == Menu.dump:
        q.dump()
    
    else :
        print("End")
        break