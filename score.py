# -*- coding: utf-8 -*-
"""Score

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rXc0if9DnswRApyqk4EZ023sv7sMPXRA
"""

a = input()
b = a.split()
p = 0
s = 0
for n in b:
  s = s + int(n)
  if int(n) < 60:
    p = p+1
avg = s/len(b)
print(avg)