

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


squares = [x ** 2 for x in numbers]

print(squares)

squares_of_even = [x ** 2 for x in numbers if x % 2 == 0]


for i, val in enumerate(squares_of_even):
    print(f"Index: {i}, Value: {val}")