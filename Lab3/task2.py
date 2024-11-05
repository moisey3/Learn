# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, rasdel=","):
    list_group = []
    for i in first_group.split(rasdel):
        for j in second_group.split(rasdel):
            if j == i:
                list_group.append(j)
    list_group.sort()
    return list_group

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants_first_group1 = "Иванов,Петров,Сидоров"
participants_second_group2 = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
print(find_common_participants(participants_first_group1, participants_second_group2))