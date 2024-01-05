import random

from domain.student import Student
from domain.student_group import StudentGroup
from domain.student_steam import StudentSteam


s1 = Student("Иван", 25)
s2 = Student("Игорь", 23)
s3 = Student("Иван", 22)
s4 = Student("Игорь", 23)
s5 = Student("Даша", 23)
s6 = Student("Лена", 23)
list_stud = [s1, s2, s3, s4, s5, s6]
group4580 = StudentGroup(list_stud, 4580)   

student1 = Student("Анна", random.randint(18, 23))
student2 = Student("Максим", random.randint(18, 23))
student3 = Student("Екатерина", random.randint(18, 23))
student4 = Student("Алексей", random.randint(18, 23))
student5 = Student("Мария", random.randint(18, 23))
student6 = Student("Сергей", random.randint(18, 23))
student7 = Student("Ольга", random.randint(18, 23))
students_list = [student1, student2, student3, student4, student5, student6, student7]
group6666 = StudentGroup(students_list, 6666)

student8 = Student("Денис", random.randint(18, 23))
student9 = Student("Алиса", random.randint(18, 23))
student10 = Student("Павел", random.randint(18, 23))
student11 = Student("Наталья", random.randint(18, 23))
student12 = Student("Владимир", random.randint(18, 23))
student13 = Student("Ангелина", random.randint(18, 23))
student14 = Student("Дмитрий", random.randint(18, 23))
new_students_list = [student8, student9, student10, student11, student12, student13, student14]
new_group = StudentGroup(new_students_list, 1234)


list_group = [group4580, group6666, new_group]
sorted_groups = sorted(list_group, key=len) # сортировка по количеству студентов в группе
steam_1 = StudentSteam(sorted_groups, 1)
print(steam_1)
for group in steam_1:
    print('\n', group)

print('========================================')

sorted_groups = sorted(list_group) 
# Отсортировано сначала по количеству студентов, а затем по идентификатору группы - реализовано по уолчанию
steam_1 = StudentSteam(sorted_groups, 1)
print(steam_1)
for group in steam_1:
    print('\n', group)
