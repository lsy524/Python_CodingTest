import time 

start_time = time.time()

def reverse_array(x):
    n = len(x)

    for i in range(n // 2):
        x[i], x[n - i - 1] = x[n - i - 1], x[i]



if __name__ == '__main__' :
    num = int(input("Input elements : ")) # 6.601647615432739
    nx = [None] * num 

    for i in range(num):
        nx[i] = int(input("Input : "))

    reverse_array(nx)

    for i in range(len(nx)):
        print(f'x[{i}] : {nx[i]}')
        
end_time = time.time()

print(end_time - start_time)