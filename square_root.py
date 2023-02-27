x = 25
number_of_guesses = 0
epsilon = .01
high = 25
low = 1
ans = (high + low) / 2

while abs(ans ** 2 - x) >= epsilon:
    number_of_guesses += 1
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (low + high) / 2
print(f"The square root of {x} is {ans}. Number of attempts required: {number_of_guesses}")
