# Generators, a simple way to do a iterator

# Generators function

def counter_generator(low, high):
    while low <= high:
       yield low
       low += 1

print("Generator function -----------------")
for i in counter_generator(5,10):
    print(i)

for i in counter_generator(5,10):
    print(i)


# # Generators expression
# print("Generator expression -----------------")
# counter_expression = (x for x in range(5, 11))
# for i in counter_expression:
#     print(i)

# print(next(counter_expression))
# print(next(counter_expression))
# print(next(counter_expression))
# print(next(counter_expression))
# print(next(counter_expression))
# print(next(counter_expression))
# print(next(counter_expression))