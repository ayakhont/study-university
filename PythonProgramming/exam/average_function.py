# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average
# Define separate functions for the input and for calculating the average


def init_vector()-> 'list':
    print("Please input 10 numbers for vector:")
    vector = list()
    for number in range(10):
        vector.append(int(input()))
    return vector


def get_average_value(vector)-> float:
    return sum(vector) / len(vector)


def print_output(vector: list, averageValue: float):
    print("The input vector:", vector)
    print("The average value of the vector: ", averageValue)


some_vector = init_vector()
averageValue = get_average_value(some_vector)
print_output(some_vector, averageValue)




