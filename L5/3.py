
marks = input('оценки через пробел')

marks = list(map(int, marks.split()))
pyaterki = marks_list.count(5)

total_marks = len(marks_list)
percent_pyaterki = (pyaterki / total_marks) * 100

print(f'процент пятерок: {perent_pyaterki}%')