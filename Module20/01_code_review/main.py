
students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

ages = []
interests = []
len_surnames = 0
for student in students:
    age = (student, students[student]['age'])
    ages.append(age)

for student in students:
    for interest in students[student]['interests']:
        interests.append(interest)
    for surname in students[student]['surname']:
        len_surnames += len(surname)

print(f'Список пар "ID студента - возраст": {ages}\n'
    f'Полный список интересов всех студентов: {interests}\n'
    f'Длина всех фамилий студентов: {len_surnames}\n'
)


#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)
#
#
