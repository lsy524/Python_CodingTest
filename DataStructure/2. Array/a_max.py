def max_of(x):
    maximum = x[0]

    for i in range(1, len(x)):
        if x[i] > maximum:
            maximum = x[i]
    
    return maximum

if __name__ == '__main__':
    num = int(input("Input elements : "))
    # 내 풀이 
    x = []

    for i in range(num):
        x.append(int(input(f'[{i+1}] : ')))

    # 예제 풀이 
    # x = [None] * num 

    # for i in range(num):
    #     x[i] = int(input(f'x[{i}] : '))
    
    print(max_of(x))