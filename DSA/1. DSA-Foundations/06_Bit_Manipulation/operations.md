# Bit Operations Reference

```python
# Set bit i
x | (1 << i)

# Clear bit i
x & ~(1 << i)

# Toggle bit i
x ^ (1 << i)

# Check bit i
(x >> i) & 1

# Power of two?
n > 0 and (n & (n - 1)) == 0

# Count set bits
bin(n).count('1')  # or Brian Kernighan: while n: n &= n-1; count++
```

## Dry run: n & (n-1)

n=12 (1100), n-1=11 (1011) → 1000 (8) — lowest set bit cleared.
