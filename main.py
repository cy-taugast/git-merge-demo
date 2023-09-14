def fibonacci(n):
    a, b = 0, 1
    fibonacci_list = []
    for i in range(n):
        a, b = b, a+b
        fibonacci_list.append(a)
    return fibonacci_list


def print_sequence(sequence):
    print(sequence)


if __name__ == '__main__':
    fibonacci_sequence = fibonacci(10)
    print_sequence(fibonacci_sequence)