n = int(input())
arr = []
for i in range(n):
    new = int(input())
    arr.append(new)
_sum_ = 0
for i in arr:
    _sum_ = _sum_ + i
print(_sum_)