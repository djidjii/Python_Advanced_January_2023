students = int(input())
students_data = {}

for _ in range(students):
    students_name, grade = input().split(' ')
    if students_name not in students_data:
        students_data[students_name] = []

    students_data[students_name].append(float(grade))

for student, grades in students_data.items():
    convert_grade_to_string = ' '.join(map(lambda grade: f'{grade:.2f}', grades))
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {convert_grade_to_string} (avg: {average_grade:.2f})")