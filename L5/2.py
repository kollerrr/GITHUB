import random

marks = []

for _ in range(4):
marks.append(random.randint(2, 5))

average_grades = sum(marks) / len(marks)

print(marks, average_grades)