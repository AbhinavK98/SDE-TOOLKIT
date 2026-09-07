# Backtracking Template

```python
def subsets(nums):
    result, path = [], []

    def backtrack(i):
        if i == len(nums):
            result.append(path[:])
            return
        path.append(nums[i])
        backtrack(i + 1)
        path.pop()
        backtrack(i + 1)

    backtrack(0)
    return result
```
