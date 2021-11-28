# Behind the for loop

from generators_2 import Counter

counter = Counter(5, 10)
iterator = iter(counter)
while True:
    try:
        x = iterator.__next__()
        print(x)
    except StopIteration as e:
        break