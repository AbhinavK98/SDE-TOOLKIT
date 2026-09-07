# Binary Search Flowchart

```
start lo=0, hi=n-1
    |
    v
 lo <= hi ? --no--> not found
    |
   yes
    |
 compute mid
    |
 arr[mid]==target? --yes--> found
    |
 arr[mid]<target? --yes--> lo=mid+1
    |
 else hi=mid-1
    |
 loop
```
