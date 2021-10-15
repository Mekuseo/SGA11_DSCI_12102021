back_in_black_rating = 8.5
if back_in_black_rating > 8.0:
    print('This Album is amazing')

back_in_black = 8.5
if back_in_black > 8.0:
    print('this album is amazing')
else:
    print('this album is ok')


def f(a, b):
    return a * b


a = 4
b = 2
if a * b == f(a, b):
    print("Correct.")
else:
    print("Incorrect.")


def g(c):
    print(sum(c))

c = [1, 2, 3, 4, 5]
if sum(c) == g(c):
    print("Correct.")
else:
    print("Incorrect.")


