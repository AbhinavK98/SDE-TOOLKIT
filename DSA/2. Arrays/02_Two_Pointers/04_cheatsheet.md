# Two Pointers Pattern Cheatsheet

    ## Recognition Clues

    - Terms like pair, target, duplicate, subarray, window, range sum
    - Constraints pushing from O(n^2) to O(n)

    ## Complexities

    | Problem | Brute | Typical Optimal |
    |---|---|---|
    | Remove Duplicates from Sorted Array | O(n^2) or problem-specific | O(n) / optimal for pattern |
| Remove Element | O(n^2) or problem-specific | O(n) / optimal for pattern |
| Merge Sorted Array | O(n^2) or problem-specific | O(n) / optimal for pattern |
| Move Zeroes | O(n^2) or problem-specific | O(n) / optimal for pattern |
| Squares of a Sorted Array | O(n^2) or problem-specific | O(n) / optimal for pattern |
| Container With Most Water | O(n^2) or problem-specific | O(n) / optimal for pattern |

    ## Common Tricks

    - Hash map lookup before insert (when needed)
    - Two pointers on sorted arrays
    - Prefix precomputation for fast range sum
    - Expand/shrink window for contiguous segments

    ## Templates

    ```python
    # HashMap template
    seen = {}
    for index, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], index]
        seen[value] = index
    ```

    ```python
    # Two pointers template
    left, right = 0, len(nums) - 1
    while left < right:
        current = nums[left] + nums[right]
        if current == target:
            return [left, right]
        if current < target:
            left += 1
        else:
            right -= 1
    ```

    ## Common Mistakes

    - Off-by-one boundaries
    - Wrong pointer direction
    - Mutating data unexpectedly
    - Forgetting empty input handling

    ## Pattern Comparison

    - HashMap: best for random lookup by value
    - Two pointers: best when sorted or in-place rearrangement
    - Prefix sum: best for repeated range sum queries
    - Sliding window: best for contiguous optimization with constraints
