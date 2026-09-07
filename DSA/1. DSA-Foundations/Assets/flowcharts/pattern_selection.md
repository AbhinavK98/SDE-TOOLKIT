# Pattern Selection Flowchart

```
Start
  |
  v
Sorted? --yes--> BS / Two pointers
  |
 no
  v
Need lookup? --yes--> HashMap
  |
 no
  v
Contiguous subarray? --yes--> Window / Prefix
  |
 no
  v
All combinations? --yes--> Backtracking
  |
 no
  v
Brute force + optimize
```
