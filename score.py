
a = input()
b = a.split()
p = 0
s = 0
for n in b:
  s = s + int(n)
  if int(n) < 60:
    p = p+1
avg = s/len(b)

=======
# 找出最大值和最小值
max_val = max(map(int, b))  # 將字串轉為整數後找最大值
min_val = min(map(int, b))  # 將字串轉為整數後找最小值

# 輸出結果
print(f"總和：{s}")
print(avg)
print(f"小於 60 的數量：{p}")
print(f"最大值：{max_val}")
print(f"最小值：{min_val}")
