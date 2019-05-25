print(len("hello"))
s = "abc"
print(s[0])

# s[20] = "k" # 'str' object does not support item assignment

# ------ slice[start:stop:step]

s = "helloworld."

print(s[3:6])  # 3, 4, 5 low
print(s[::-1])  # .dlrowolleh

# strings are immutable  - cannot be modified.


for char in s:
    if char == 'l' or char == 'o':
        print(":-(")
