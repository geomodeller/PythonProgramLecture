# list & for-statement
score = [88, 95, 70, 100, 99]

sum = 0
for s in score:
    sum += s
print(f'총점: {sum} 점')
print(f'평균: {sum/len(score):.2f} 점')