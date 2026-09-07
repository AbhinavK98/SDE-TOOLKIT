# Complexity Charts

Visual reference for growth rates (n = input size).

---

## Growth Rate Chart (relative)

```
Operations
    ^
    |                                    O(n!)
    |                               O(2^n)
    |                          O(n^2)
    |                    O(n log n)
    |              O(n)
    |        O(log n)
    |   O(1)________________________________> n
```

---

## Practical limits (rough interview guide)

| n | Max typical complexity |
|---|----------------------|
| ≤ 10 | O(n!), O(2^n) |
| ≤ 20 | O(2^n) |
| ≤ 500 | O(n³) |
| ≤ 5000 | O(n²) |
| ≤ 10^5 | O(n log n) |
| ≤ 10^6 | O(n) or O(n log n) |
| ≤ 10^8 | O(n) or O(log n) |

---

## Loop pattern cheat chart

| Pattern | Complexity |
|---------|------------|
| `for i in n` | O(n) |
| `for i in n: for j in n` | O(n²) |
| `for i in n: j = n; while j: j//=2` | O(n log n) |
| `while n: n//=2` | O(log n) |
| Recursion T(n)=2T(n/2)+O(n) | O(n log n) |
| Recursion T(n)=T(n-1)+O(1) | O(n) |
| Recursion T(n)=2T(n-1) | O(2^n) |

---

## Space chart

| Algorithm | Auxiliary space |
|-----------|-----------------|
| Bubble sort | O(1) |
| Merge sort | O(n) |
| DFS recursion | O(h) height |
| BFS queue | O(width) |
| DP table n×m | O(n·m) |

---

## Assets

Additional diagrams: [../Assets/charts/complexity_growth.md](../Assets/charts/complexity_growth.md)
