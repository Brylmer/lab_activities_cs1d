def find_smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                print(f"The smallest factor of {n} is: {i}")
                break

try:
    n = int(input("Enter an integer (>= 2): "))
    find_smallest_factor(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")