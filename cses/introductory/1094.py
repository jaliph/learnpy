
n = int(input())
nums = [ int(num) for num in input().split() ]

cost = 0

for i in range(1, len(nums)):
  if nums[i - 1] > nums[i]:
    cost += nums[i - 1] - nums[i]
    nums[i] = nums[i - 1]

print(cost)
