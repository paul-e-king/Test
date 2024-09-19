a = "Hello"
b = "Hello"
print("location of a =", id(a))
print("location of b =", id(b))
print(a is b)
a = a.replace("e","z")
print(a)
print(b)
print(a is b)
print("location of a =", id(a))
print("location of b =", id(b))
