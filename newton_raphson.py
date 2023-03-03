epsilon = .01
y = 24
guess = 24/2.0
num_of_guesses = 0
while abs(guess**2 - y) >= epsilon:
    num_of_guesses += 1
    guess = guess - ((guess**2 - 24)/(2*guess))
print(f"number of guesses {num_of_guesses}")
print(f"The square root of {y} is {guess}")

