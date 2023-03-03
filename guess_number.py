low = 0
high = 100
ans = (low + high) / 2
print("Please think a number between 0 and 100!")
while True:
    print("Is your secret number", int(ans), "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                  "Enter 'c' to indicate I guessed correctly.")
    if guess == 'c':
        print("Game over. Your secret number was:", ans)
        break
    elif guess == 'h':
        high = ans
    elif guess == 'l':
        low = ans
    else:
        print("Sorry, I did not understand your input.")
    ans = int((low + high)/2)


