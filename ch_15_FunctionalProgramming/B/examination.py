# let suppose a dictionary named students contains the names and marks respectivly
students = {
    "Aaditay": 78,
    "Abhay": 90,
    "Sachin": 67,
    "Faizal": 78,
    "Fiza": 96,
    "Vishal": 34,
    "Smriti": 39,
    "Tanishk": 41,
}

lst = filter(lambda n: n[1] >= 40, students.items())

print(list(lst))
