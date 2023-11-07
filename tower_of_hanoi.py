def print_move(fr, to):
    print(f"Move disk from {str(fr)} to {str(to)}")


def tower_of_hanoi(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        tower_of_hanoi(n - 1, fr, spare, to)
        tower_of_hanoi(1, fr, to, spare)
        tower_of_hanoi(n - 1, spare, to, fr)


tower_of_hanoi(3, "A", "B", "SPARE")
