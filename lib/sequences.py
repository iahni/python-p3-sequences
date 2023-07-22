#!/usr/bin/env python3

def print_fibonacci(length):
    sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    if length < 2:
        sequence = sequence[:length]  # Adjust the sequence length if it's less than 2
    else:
        while len(sequence) < length:  # Generate the Fibonacci sequence up to the desired length
            next_num = sequence[-1] + sequence[-2]
            sequence.append(next_num)

    print(sequence)

print_fibonacci(9)