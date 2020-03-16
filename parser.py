import requests as r
import re

c = 0
first = input()
final = input()
first = r.get(first)
first = first.text
x = r'<a href.*?".*?"'
z = re.findall(x, first)
for m in z:
    m1 = str(m)
    s = m1.find('"')
    m1 = m1[s+1:-1]
    page = r.get(m1)
    page = page.text
    for n in re.findall(x, page):
          n1 = str(n)
          s = n1.find('"')
          n1 = n1[s+1:-1]
          if n1 == final:
            print('Yes')
            c += 1
            break
    if c > 0:
      break
if c == 0:
  print('No')
