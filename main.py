import math
import colorama
from colorama import Fore, Style, init

init()


def color_text(number, text, color):
    return f"{number}: {color}{text}{Style.RESET_ALL}"


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0:
            return False
    return True


def prime_factors(number):
    factors = []
    for i in range(2, number + 1):
        if number % i == 0 and is_prime(i):
            factors.append(i)
    return factors


def prime_factorization(number, factors):
    factorization = {}
    for factor in factors:
        count = 0
        while number % factor == 0:
            number //= factor
            count += 1
        if count > 0:
            factorization[factor] = count
    return factorization


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)


def is_perfect(number):
    if number < 1:
        return False

    divisors = []
    for i in range(1, (number // 2) + 1):
        if number % i == 0:
            divisors.append(i)

    return sum(divisors) == number


def main():
    error_input = f"{Fore.RED}Invalid input. Please enter a positive integer greater than 1.{Style.RESET_ALL}"
    while True:
        try:
            choice = int(
                input("Select an option:\n"
                      f"{color_text(1, 'Prime Factors', Fore.GREEN)} \n"
                      f"{color_text(2, 'Display Prime Fractions', Fore.YELLOW)}\n"
                      f"{color_text(3, 'Greatest Common Denominator', Fore.BLUE)}\n"
                      f"{color_text(4, 'Least Common Multiple', Fore.MAGENTA)}\n"
                      f"{color_text(5, 'Check Perfectness', Fore.CYAN)}\n"
                      f"{color_text(6, 'Quit', Fore.WHITE)}\n"))

            if choice == 1:
                print(f"{Fore.GREEN}The factors of a number that themselves are indivisible.{Style.RESET_ALL}")
                number = int(input(f"{Fore.GREEN}Enter a positive integer: {Style.RESET_ALL}"))
                if number < 1:
                    print(error_input)
                else:
                    factors = prime_factors(number)
                    print(f"{Fore.GREEN}Prime factors of {number:,}: {', '.join(map(str, factors))}{Style.RESET_ALL}")

            elif choice == 2:
                print(f"{Fore.YELLOW}Displays the multiplication required.{Style.RESET_ALL}")
                number = int(input(f"{Fore.YELLOW}Enter a positive integer: {Style.RESET_ALL}"))
                if number < 1:
                    print(error_input)
                else:
                    factors = prime_factors(number)
                    factorization = prime_factorization(number, factors)
                    print(
                        f"{Fore.YELLOW}Prime factorization of {number:,}: ({') * ('.join([f'{k}^{v}' for k, v in factorization.items()])}){Style.RESET_ALL}")

            elif choice == 3:
                print(f"{Fore.BLUE}The Greatest Common Denominator is the largest factor that two or more numbers "
                      f"have in common.{Style.RESET_ALL}")
                a = int(input(f"{Fore.BLUE} the first positive integer: {Style.RESET_ALL}"))
                b = int(input(f"{Fore.BLUE}Enter the second positive integer: {Style.RESET_ALL}"))
                if a < 1 or b < 1:
                    print(error_input)
                else:
                    gcd = find_gcd(a, b)
                    print(f"{Fore.BLUE}The Greatest Common Denominator of {a:,} and {b:,} is: {gcd:,}{Style.RESET_ALL}")

            elif choice == 4:
                print(f"{Fore.MAGENTA}The Least Common Multiple is the smallest multiple that two or more numbers "
                      f"have in common{Style.RESET_ALL}")
                a = int(input(f"{Fore.MAGENTA}Enter the first positive integer: {Style.RESET_ALL}"))
                b = int(input(f"{Fore.MAGENTA}Enter the second positive integer: {Style.RESET_ALL}"))
                if a < 1 or b < 1:
                    print(error_input)
                else:
                    lcm = find_lcm(a, b)
                    print(f"{Fore.MAGENTA}The Least Common Multiple of {a:,} and {b:,} is: {lcm:,}{Style.RESET_ALL}")

            elif choice == 5:
                print(f"{Fore.CYAN}A perfect number is a positive integer that is equal to the sum of its proper "
                      "divisors ("
                      f"excluding itself).{Style.RESET_ALL}")
                number = int(input(f"{Fore.CYAN}Enter a positive integer: {Style.RESET_ALL}"))
                if number < 1:
                    print(error_input)
                else:
                    if is_perfect(number):
                        print(f"{Fore.CYAN}{number:,} is a perfect number.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.CYAN}{number:,} is not a perfect number.{Style.RESET_ALL}")

            elif choice == 6:
                print(f"{Fore.WHITE}Exiting...{Style.RESET_ALL}")
                break

            else:
                print(f"{Fore.RED}Invalid choice. Please enter a number 1-6:{Style.RESET_ALL}")

        except ValueError:
            print(error_input)


if __name__ == "__main__":
    main()
