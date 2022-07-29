import sys
w, h, b = map(int, sys.stdin.readline().split())

print(f'{w * h * b / 8/ 1024 / 1024 :.2f}', "MB")