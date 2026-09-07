# Bit Manipulation Patterns

| Pattern | Technique |
|---------|-----------|
| Single number | XOR all |
| Power of 2 | n & (n-1) == 0 |
| Subset generation | Mask 0..2^n-1 |
| Swap without temp | a^=b; b^=a; a^=b (rare in interviews) |
| Get/set/toggle bit | shifts + masks |

## Subset bitmask ASCII

n=3 elements, mask 0..7:

```
mask 101 -> pick items 0 and 2
```
