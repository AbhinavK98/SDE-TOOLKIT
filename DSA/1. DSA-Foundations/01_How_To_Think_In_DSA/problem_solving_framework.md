# Problem Solving Framework

Use this **every time** you see a new problem.

---

## Step 1: Understand (WHAT)

**WHY:** You cannot solve what you do not understand.

**HOW:**
1. Restate the problem in your own words.
2. Identify input and output types.
3. Ask: "What is the smallest valid input?"

**Example:** Two Sum — "Given numbers and a target, return indices of two numbers that add to target."

---

## Step 2: Constraints (WHEN)

**WHY:** Constraints tell you which algorithm is fast enough.

| Constraint hint | Likely approach |
|-----------------|-----------------|
| n ≤ 10^5 | O(n) or O(n log n) |
| n ≤ 20 | O(2^n) backtracking OK |
| Sorted array | Binary search, two pointers |
| Subarray | Prefix sum, sliding window |

---

## Step 3: Examples (HOW to verify)

Write **at least 3** examples:
- Normal case
- Edge case (empty, one element)
- Tricky case (duplicates, negatives)

Dry-run your future algorithm on paper.

---

## Step 4: Brute Force (WHY first)

**WHY:** Proves you understand the problem. Gives a correctness baseline.

**HOW:** Nested loops, try all possibilities.

**WHEN:** Always mention in interviews before optimizing.

---

## Step 5: Optimize (HOW)

Ask:
- What work is repeated?
- Can I remember past results? → Hash map
- Is data sorted? → Two pointers / binary search
- Is it contiguous? → Sliding window

---

## Step 6: Code (WHAT)

- Meaningful names
- Handle edge cases first
- One clear invariant per loop

---

## Step 7: Test & Explain

Walk through one example line by line. State time and space complexity with **reason**.

---

## ASCII: Full Flow

```
   +-------------+
   | Read Problem|
   +------+------+
          |
          v
   +-------------+     +--------------+
   | Constraints |---->| Pick Big-O   |
   +-------------+     +--------------+
          |
          v
   +-------------+     +--------------+
   |  Examples   |---->| Dry Run      |
   +-------------+     +--------------+
          |
          v
   +-------------+     +--------------+
   | Brute Force |---->| Bottleneck?  |
   +-------------+     +--------------+
          |
          v
   +-------------+
   |  Optimal    |
   +-------------+
```

---

## Common Mistakes

- Coding before understanding
- Ignoring constraints
- Skipping edge cases
- Not explaining complexity

---

## Interview Tips

- "Let me start with a brute force, then optimize."
- "My invariant is: left pointer always marks..."
- Pause before coding — interviewers prefer clarity over speed.
