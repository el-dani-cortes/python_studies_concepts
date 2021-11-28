# Iterators vs iterable

x = [1, 2, 3]

y = iter(x)
z = iter(x)

print(f"y={next(y)}")
print(f"y={next(y)}")
print(f"y={next(y)}")
try:
    print(f"y={next(y)}")
except:
    print(f"y={next(y)}")

print(f"z={next(z)}")

print(type(x))
print(type(y))
print(type(z))

print(dir(x))
print(dir(y))