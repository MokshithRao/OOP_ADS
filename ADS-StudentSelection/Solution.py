from functools import cmp_to_key
from datetime import datetime


class Student:
    def __init__(self, name, dob, sub1, sub2, sub3, total_marks, category):
        self.name = name
        self.dob = dob
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.total_marks = total_marks
        self.category = category


    def __str__(self):
        return f"{self.name},{self.total_marks},{self.category}"
    


def compare(s1, s2):
    if s1.total_marks > s2.total_marks:
        return -1
    elif s1.total_marks < s2.total_marks:
        return 1

    if s1.sub3 > s2.sub3:
        return -1
    elif s1.sub3 < s2.sub3:
        return 1

    if s1.sub2 > s2.sub2:
        return -1
    elif s1.sub2 < s2.sub2:
        return 1

    if s1.dob > s2.dob:
        return -1
    elif s1.dob < s2.dob:
        return 1

    if s1.name < s2.name:
        return -1
    elif s1.name > s2.name:
        return 1

    return 0



total_students = int(input())
total_vacancies = int(input())
unreserved_vacancies = int(input())
bc_vacancies = int(input())
sc_vacancies = int(input())
st_vacancies = int(input())

students = []


for i in range(total_students):
    s = input().strip().split(",")
    dob = datetime.strptime(s[1], "%d-%m-%Y")
    students.append(Student(s[0], dob, int(s[2]), int(s[3]), int(s[4]), int(s[5]), s[6]))

students.sort(key=cmp_to_key(compare))

for i in students:
    print(i)
print()


selected = []
bc_selected = []
sc_selected = []
st_selected = []
open_selected = []
remaining_candidates = []

unc = unreserved_vacancies
for i in students[:]:
    if unreserved_vacancies > 0:
        open_selected.append(i)
        students.remove(i)
        unreserved_vacancies -= 1
    else:
        break
    
for student in students[:]:
    if bc_vacancies > 0 and student.category == "BC":
        bc_selected.append(student)
        students.remove(student)
        bc_vacancies -= 1

if bc_vacancies > 0:
    for student in students[:]:
        if bc_vacancies > 0:
            bc_selected.append(student)
            students.remove(student)
            bc_vacancies -= 1

for student in students[:]:
    if sc_vacancies > 0 and student.category == "SC":
        sc_selected.append(student)
        students.remove(student)
        sc_vacancies -= 1

if sc_vacancies > 0:
    for student in students[:]:
        if sc_vacancies > 0:
            sc_selected.append(student)
            students.remove(student)
            sc_vacancies -= 1

for student in students[:]:
    if st_vacancies > 0 and student.category == "ST":
        st_selected.append(student)
        students.remove(student)
        st_vacancies -= 1

if st_vacancies > 0:
    for student in students[:]:
        if st_vacancies > 0:
            st_selected.append(student)
            students.remove(student)
            st_vacancies -= 1

selected = open_selected + bc_selected + sc_selected + st_selected
selected.sort(key=cmp_to_key(compare))
for student in selected:
    print(student)






