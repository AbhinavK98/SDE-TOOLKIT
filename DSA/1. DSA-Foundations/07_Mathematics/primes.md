# Primes & Sieve

## WHAT

Prime has exactly two divisors: 1 and itself.

## Sieve of Eratosthenes — O(n log log n)

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime
```

## WHY start j at i*i

Smaller multiples already marked by smaller primes.
