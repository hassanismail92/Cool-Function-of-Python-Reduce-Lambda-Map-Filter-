#Program for using Reduce, lambda, filter and map

from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,23,24,26,34,35]

even = list(filter(lambda x: x % 2 == 0, numbers))

print("The EVEN Numbers are", even)

odd = list(filter(lambda x: x % 2 != 0, numbers))
print("The ODD Numbers are", odd)

double = list(map(lambda x: x*2, even))
print("The Doubles of the even are Numbers are", double)

ans = reduce(lambda a, b: a + b, double)
print("The Sumition of Doubles Numbers are", ans)