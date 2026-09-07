# Binary Search Variations

---

## Binary Search on Answer

**WHEN:** Minimize/maximize value such that condition becomes true (monotonic).

**HOW:** BS on answer range, check feasibility with helper.

**Example:** Minimum capacity to ship packages in D days.

---

## Lower Bound (first >= target)

First index where `arr[i] >= target`.

```python
def lower_bound(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

---

## Upper Bound (first > target)

Similar; adjust comparison.

---

## First / Last Occurrence

- First: when `arr[mid]==target`, hi = mid (don't stop)
- Last: when equal, lo = mid + 1

---

## Search in Rotated Sorted Array

Check which half is sorted; decide which side contains target.

---

## Peak Element

`arr[mid] < arr[mid+1]` → peak on right, else left.

---

## Templates summary

| Goal | Move when |
|------|-----------|
| Exact match | Standard BS |
| First >= | hi = mid on candidate |
| Last <= | lo = mid on candidate |
| Answer space | BS on value + check() |

## Common Mistakes

- BS on unsorted array
- Non-monotonic check function in BS on answer
