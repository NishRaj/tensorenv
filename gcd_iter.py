def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        return a
    min_val = a if a < b else b
    while True:
        if min_val == 1:
            return min_val
        elif a % min_val == 0 and b % min_val == 0:
            return min_val
        min_val -= 1
