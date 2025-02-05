
s = input()
prev = ''
count = 0
m = 0

for ch in s:
  if prev != ch:
    prev = ch
    count = 1
  else:
    count = count + 1
  m = max(m, count)


print(m)
