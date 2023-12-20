#!/usr/bin/python3

def factorize_rsa_number(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

def main():
    with open("tests/rsa-1", "r") as file:
        rsa_number = int(file.readline().strip())

    prime_factors = factorize_rsa_number(rsa_number)

    print(f"{rsa_number}=", "*".join(map(str, prime_factors)))

if __name__ == "__main__":
    main()
