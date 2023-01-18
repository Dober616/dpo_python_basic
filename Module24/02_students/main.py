class Student:

    def __init__(self, full_name, groupe, marks):
        self.full_name = full_name
        self.groupe = groupe
        self.marks = marks
        self.average = sum(marks) / len(marks)

    def marks_average(self):
        return self.average

    def best_students(self):
        good_marks = list(filter(lambda x: x in [4, 5], self.marks))
        return self.marks == good_marks


def student_data():
    name = input('Введите имя: ')
    groupe = input('Номер группы: ')
    marks = list(map(int, input('Оценки через пробел: ').split()))
    return name, groupe, marks


student_list = [Student(*student_data()) for _ in range(3)]
student_list.sort(key=lambda x: x.marks_average(), reverse=True)
print('Средние оценки студентов по убыванию:')
for student in student_list:
    print(f'Студент: {student.full_name}, группа: {student.groupe}, '
          f'оценки: {student.marks}, средняя оценка: {student.average}')
print('Студенты с хорошими оценками: ')
for student in student_list:
    if student.best_students():
        print(f'Студент: {student.full_name}, группа: {student.groupe}, '
              f'оценки: {student.marks}, средняя оценка: {student.average}')
