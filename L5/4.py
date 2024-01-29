
data = []

surname = input('фамилия ')
position = input('должность ')
students_count = input('количество студентов через запятую ')

student_counts_list = list(map(int, student_counts.split(',')))

data.append([surname, position, student_counts_list])

print(data)
