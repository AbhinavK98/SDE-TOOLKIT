# GCD and LCM

## Euclidean GCD — O(log min(a,b))

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

## LCM

lcm(a,b) = a * b // gcd(a,b)

## WHY Euclidean works

gcd(a,b) = gcd(b, a % b) — remainder preserves common divisors.
