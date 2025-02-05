
n = int(input())
nums = [ int(i) for i in input().split() ]
act = sum(nums)
exp = n * (n + 1) // 2
print(exp - act)

