def  list_all_primes_below(limit):
    list_of_primes = []
    number = 2
    while number <= limit:
            is_prime(number)
            number += 1
    return list_of_primes

def  list_first_X_primes(X):
    list_of_primes = []
    number = 2
    while len(list_of_primes) < X:
            is_prime(number)
            number += 1
    return list_of_primes
def is_prime(number):
    for prime in list_of_primes:
        if number % prime == 0:
            #not prime
            return False
    store_prime(number)
    return True
def store_prime(prime):
    list_of_primes.append(prime)

if __name__ == "__main__":
    #print(list_all_primes_below(10000))
    print(list_first_X_primes(10001))
