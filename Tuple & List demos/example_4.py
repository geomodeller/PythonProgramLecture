# list of list (nested list)
score = [
    [90, 80, 60, 77],
    [99, 56, 75, 80],
    [100, 90, 50, 30]
]

total = 0
total_count = 0

for student in score:
    sum = 0
    for subject in student:
        sum += subject
    print(f'총점 {sum} 점 || 평균 {sum/len(student)}')
    total += sum
    total_count += len(student)

print(f'... 총 평균은 {total/total_count:.3f} 점')