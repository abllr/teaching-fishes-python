# Reverse Function
def reverse(string):
    return(string[::-1])

# Palindrome
def palindrome(string):
    if string == reverse(string):
        return True
    else:
        return False

# Palindromer
def palindromer(lst):
    results = []
    for x in lst:
        if palindrome(x):
            results.append(True)
        else:
            results.append(False)

# Sieve of Erasthotenes
def SieveOfEratosthenes(n):
    # Fill list up to number with all nums defaulted to True
    prime = [True for x in range(n+1)]
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            # Set all non-prime number to False (multiplying p by itself)
            for x in range(p * p, n + 1, p):
                prime[x] = False
        p += 1            
    # Prints index of all True values in prime
    for p in range(2, n):
        if prime[p]:
            print(p)

SieveOfEratosthenes(1000)          
