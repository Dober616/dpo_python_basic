general_list = []
first_class_list = []
second_class_list = []
for height in range(160,177,2):
    first_class_list.append(height)
for height in range(162,181,3):
    second_class_list.append(height)
first_class_list.extend(second_class_list)
first_class_list.sort()
print('Отсортированный список учеников: ',first_class_list)
