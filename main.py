def fibonacci(n):
    fibonacci_list =[]
    for i in range(n):
        if i == 1 or i == 0:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[i-2]+fibonacci_list[i-1])
    return fibonacci_list


def print_sequence(sequence):
    for num in sequence:
        print(num)


if __name__ == '__main__':
    fibonacci_sequence = fibonacci(10)
    print_sequence(fibonacci_sequence)