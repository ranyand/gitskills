o = ""
for each in text:
    if ord(each) >= ord('a') and ord(each) <= ord('z'):
        o += chr((ord(each) + 2 - ord('a')) % 26 + ord('a')) # 尝试理解该转换公式
    else:
        o += each
print o
