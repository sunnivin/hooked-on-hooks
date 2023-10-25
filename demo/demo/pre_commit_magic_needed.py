import sys
import random
def generate_random_numbers(n: int) -> list[int]:
    numbers = [random.randint(1, 100) for _ in range(n)]
    return numbers
def main(n: int):
    numbers = generate_random_numbers(   n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python random_numbers.py <number_of_numbers>")
        sys.exit(1)
    n = int(sys.argv[1])
    main(n)
