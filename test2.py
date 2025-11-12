import time
first = 'abcdefghi'
second = '12345678'
print(first, end='', flush=True)
for char in second:
    print(char, end="", flush=True)
    time.sleep(0.3)