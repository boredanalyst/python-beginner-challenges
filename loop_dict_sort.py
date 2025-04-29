## This loops through a dictionary in an alphabetical order.

student_grades = {
    "Angela" : 89,
    "David" : 90,
    "Carlson" : 87,
    "Quincy" : 88,
    "Martin" : 95,
    "Floyd" : 88,
    "Archie" : 90
}

## this loops through the student grades in an unsorted way.

print("###---UNSORTED VALUES---###")

for name,grade in student_grades.items():
    print(f'{name.title()} : {grade}')

print("###---SORTED VALUES---###")

for name in sorted(student_grades.keys()):
    print(f'{name.title()} : {grade}')