a = input("請輸入數字（以空格分隔）：")
b = a.split()  # 將輸入的字串以空格分割為列表
p = 0  # 計算小於 60 的數字個數
s = 0  # 總和
for n in b:
    s = s + int(n)  # 將每個數字加總
    if int(n) < 60:
        p = p + 1  # 如果數字小於 60，計數加 1


# 找出最大值和最小值
max_val = max(map(int, b))  # 將字串轉為整數後找最大值
min_val = min(map(int, b))  # 將字串轉為整數後找最小值

# 輸出結果
print(f"總和：{s}")

print(f"小於 60 的數量：{p}")
print(f"最大值：{max_val}")
print(f"最小值：{min_val}")
