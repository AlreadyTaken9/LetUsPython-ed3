dict = {
    "Danny": {"last_name": "Daniels", "age": 30, "Grade": "Highly Skilled"},
    "Sunil": {"last_name": "Kumar", "age": 24, "Grade": " Skilled"},
    "Akshay": {"last_name": "Kumar", "age": 47, "Grade": "Semi Skilled"},
    "Aman": {"last_name": "Kuntal", "age": 18, "Grade": " Skilled"},
    "Ritesh": {"last_name": "Kuntal", "age": 22, "Grade": "Highly Skilled"},
    "Lakshya": {"last_name": "Parashar", "age": 27, "Grade": "Semi Skilled"},
}

lst = filter(lambda n: n[1]["Grade"] == "Highly Skilled", dict.items())

print(list(lst))
