import string
import time

s = "Buy 1 get 2 free"
start = time.time()
nl = [c for c in s if c.isdigit()][-1]
print(nl)
end = time.time()
print(end - start)

start = time.time()
s = s.replace(" ", "")
for i in range(len(s) - 1, 1, -1):
    if s[i].isdigit():
        print(s[i])
        break
end = time.time()
print(end - start)


def cipher(a_string: str, key: int) -> str:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ""

    for c in a_string:
        if c in uppercase:
            new = (uppercase.index(c) + key) % len(uppercase)
            encrypt += uppercase[new]
        elif c in lowercase:
            new = (lowercase.index(c) + key) % len(lowercase)
            encrypt += lowercase[new]
        else:
            encrypt += c
    return encrypt


print(cipher("zakashi", 3))

words = [
    "selftaught",
    "code",
    "sit",
    "eat",
    "programming",
    "dinner",
    "one",
    "two",
    "coding",
    "a",
    "tech",
]
print([char for char in words if len(char) >= 4])
