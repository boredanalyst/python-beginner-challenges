## This loops through a dictionary of names and whether they submitted their assignments.

assignment_a = {
    "Angel" : "SUBMITTED",
    "Flor" : "SUBMITTED",
    "Jake" : "",
    "Floyd" : "",
    "Mark" : "SUBMITTED",
    "Gabby" : "SUBMITTED",
    "Flint" : "",
    "Arthur": "SUBMITTED"
}

for name in assignment_a.keys():
    if assignment_a[name] == "":
        print(f'{name.upper()} has not submitted their assignment yet!')
        print("##--------##")