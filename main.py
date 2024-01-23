# Estoy viendo el tema de imprimir la serie con un imput desde el inicio
#hasta el final
# 
print("Hello world")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(low, high):
    prime_numbers = [num for num in range(low, high + 1) if is_prime(num)]
    return prime_numbers

# Input: lowest and highest numbers
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))

# Find and print prime numbers in the specified range
prime_numbers = find_primes_in_range(low, high)
print(f"Prime numbers between {low} and {high}: {prime_numbers}")


#Pendiente guardarlo como .txt :<