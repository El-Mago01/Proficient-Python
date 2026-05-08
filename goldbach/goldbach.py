"""
This program checks if a given number can be expressed as the sum of 
two prime numbers.
The user is prompted to enter a number, and the program will first 
calculate all available pairs of prime numbers.Then it will output 
only the single pairs of prime numbers that sum up to the given number.
E.g. if the user enters 10, the program will calculate all pairs of prime 
numbers that sum up to 10, which are (3, 7), (5, 5) and (7, 3). Then it will 
output only the single pairs of prime numbers, which are (3, 7) and (5, 5).
"""

def cleanup(list_of_tuples) -> list:
    """This function removes duplicate pairs of primes from the list of tuples.
    Args:     list_of_tuples (list): A list of tuples, where each tuple contains two prime numbers.
    Returns:  list: A list of unique tuples, where each tuple contains two prime numbers.
    """
    unique_tuples = set()
    for prime_1, prime_2 in list_of_tuples:
        # Sort the pair to ensure (3, 5) and (5, 3) are considered the same
        sorted_pair = tuple(sorted((prime_1, prime_2)))
        unique_tuples.add(sorted_pair)
    return list(unique_tuples)

def enter_a_number() -> int:
    """This function prompts the user to enter a number and validates the input.
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            if number < 0:
                raise ValueError("Negative numbers are not allowed. Please " \
                "enter a non-negative integer.")
            return number
        except ValueError as e:
            print("Invalid input:", e)


def is_prime(n):
    """This function checks if a number is prime.
    Args:     n (int): The number to check.
    Returns:  bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def is_sum_of_two_primes(number_to_check : int)-> list:
    """This function checks if a number can be expressed as the sum of two 
    prime numbers. I.e. number_to_check = prime_ + prime_2.
    Args:     number (int): The number to check.
    Returns:  bool: True if the number can be expressed as the sum of 
              two prime numbers, False otherwise.
    """
    combinations_of_primes_found = []
    if number_to_check % 2 == 1:
        # odd numbers cannot be expressed as the sum of two prime numbers
        return combinations_of_primes_found
    for prime_1 in range(2, number_to_check):
        # check if prime_1 is indeed a prime
        if is_prime(prime_1):
            # prime_1 is a prime, now check if prime_2=number_to_check-prime_1
            # is a prime
            prime_2 = number_to_check - prime_1
            if prime_2 >= 2:  # prime_2 must be greater or equal 2 to be prime
                if is_prime(prime_2):
                    combinations_of_primes_found.append((prime_1, prime_2))
    return combinations_of_primes_found


def main():
    """This is the main function that runs the program."""
    number = enter_a_number()
    possible_combinations_of_primes = is_sum_of_two_primes(number)
    single_pair_of_primes = cleanup(possible_combinations_of_primes)
    if len(single_pair_of_primes) == 0:
        print(f"The number {number} cannot be expressed as the sum of two prime numbers."   )
    else:
        for prime_1, prime_2 in single_pair_of_primes:
            print(f"The number {number} equals to the sum of {prime_1} and {prime_2}")


if __name__ == "__main__":
    main()
