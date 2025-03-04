Given A and B two interval lists, A has no overlap inside A and B has no overlap inside B. Write the function to merge two interval lists, output the result with no overlap. Ask for a very efficient solution


A naive method can combine the two list, and sort and apply merge interval in the leetcode, but is not efficient enough.


For example,
A: [1,5], [10,14], [16,18]  
B: [2,6], [8,10], [11,20]  


output [1,6], [8, 20]

```python
def mergeTwoIntervalLists(first, second):
    def help(res, arr):
        if not res:
            res.append(arr)
            return
        if arr[0] > res[-1][1]:
            res.append(arr)
            return
        else:
            res[-1][1] = max(res[-1][1], arr[1])
    res = []
    i, j = 0,0
    while i <len(first) and j < len(second):
        if first[i] <= second[j]:
            help(res, first[i])
            i += 1
        else:
            help(res, second[j])
            j += 1
    while i < len(first):
        help(res, first[i])
        i += 1
    while j < len(second):
        help(res, second[j])
        j += 1
    return res

A = [[1,5],[10,14],[16,18]]
B = [[2,6],[8,10],[11,20]]

print (mergeTwoIntervalLists([[1,5], [10,14], [16,18]], [[2,6], [8,10], [11,20]]))
print (mergeTwoIntervalLists([[1,15], [10,14], [16,18]], [[2,16], [8,10], [11,20]]))
print (mergeTwoIntervalLists([[1,15], [20,24], [36,48]], [[15,15], [28,30]]))
print (mergeTwoIntervalLists([[1,15], [20,24], [36,48]], [[15,15], [28,36]]))
```
### Output
```
[[1, 6], [8, 20]]
[[1, 20]]
[[1, 15], [20, 24], [28, 30], [36, 48]]
[[1, 15], [20, 24], [28, 48]]
```
