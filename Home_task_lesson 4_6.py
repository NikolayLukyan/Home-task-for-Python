from itertools import cycle, count
your_count = count(3)
your_cycle = cycle('GFRErttyyu')
for _ in range(6):
    print("(your_count, your_cycle) = ({},{})".format(next(your_count), next(your_cycle)))
