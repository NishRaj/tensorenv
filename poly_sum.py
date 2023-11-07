import math


def polysum(n, s) -> float:
    numerator = 0.25 * n * (s ** 2)
    denominator = math.tan(math.pi / n)
    area = numerator / denominator
    perimeter = n*s
    result = area + perimeter**2
    return round(result, 4)


