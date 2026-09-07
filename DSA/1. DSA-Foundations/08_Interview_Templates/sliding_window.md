# Sliding Window Template

```python
def variable_window(nums, target):
    left = 0
    window_sum = 0
    best = float('inf')
    for right, val in enumerate(nums):
        window_sum += val
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return best if best != float('inf') else 0
```
