from functools import reduce


result = reduce(lambda accum, i: accum * i, range(100, 1001))
print('Произведение чисел от 100 до 1000 включительно равно', result)
