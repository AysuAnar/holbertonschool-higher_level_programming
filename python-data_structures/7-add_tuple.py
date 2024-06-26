#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by adding zeros if necessary
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]
    # Add the corresponding elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
