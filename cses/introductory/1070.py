
n = int(input())
# n = 3
# l = []
# from functools import lru_cache

# @lru_cache(None)
# def recursion(mask, l) -> bool: 
#   l = list(l)
#   if ((1 << n) - 1) == mask:
#     print(l)
#     return True

#   for num in range(1, n + 1):
#     if len(l) == 0 or (((mask & (1 << (num - 1)))== 0) and abs(l[-1] - num) > 1):
#       l.append(num)
#       if recursion(mask | (1 << (num - 1)), tuple(l)) is True:
#         return True
#       l.pop()

#   return False

# result = recursion(0, tuple())
# if not result: 
#   print('NO SOLUTION')

if n == 1:
  print(1)
elif n <= 3:
  print("NO SOLUTION")
else:
  odd = []
  even = []
  for num in range(n, 0, -1):
    if num & 1 == 0:
      even.append(num)
    else:
      odd.append(num)


  print(*(odd + even)) 
