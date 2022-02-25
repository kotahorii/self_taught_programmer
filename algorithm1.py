import time

start = time.time()


def t():
    for i in range(1, 6):
        yield i


for i in t():
    print(i)
end = time.time()
print(start - end)
