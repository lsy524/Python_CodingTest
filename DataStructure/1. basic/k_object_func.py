n = 1

def put_id() :
    n = 1
    print(f'id(x) = {id(n)}')


x = put_id()

if id(x) == id(n) :
    print("Permutations")
else :
    print("Combinations") 


    