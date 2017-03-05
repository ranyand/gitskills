total = 500000.0
interest = (0.01,0.02,0.03,0.035)
repay = 30000.0
i = 0
for year in interest:
    while total > 0:
        i = i + 1
        if i == 1:
            inte = 0.01
        if i == 2:
            inte = 0.02
        if i == 3:
            inte = 0.03
        if i == 4:
            inte = 0.035
        else:
            inte = 0.05
        total = total * (1 + inte) - repay

print(i+1)
