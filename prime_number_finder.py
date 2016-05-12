# Prime number finder!

list_of_primes = []
def  main():
    number = 2
    while number <= 1000000:
            is_prime(number)
            number += 1
    print list_of_primes
def is_prime(number):
    for prime in list_of_primes:
        if number % prime == 0:
            #not prime
            return False
    store_prime(number)
    return True
def store_prime(prime):
    list_of_primes.append(prime)

main()
