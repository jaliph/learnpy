
n = int(input())

res = []

while n != 1:
  print(n, end=" ")
  if n & 1 != 1:
    n = n // 2
  else:
    n = n * 3 + 1
print(n) 
