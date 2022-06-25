lst_employee = [
    "Aaditya Vikram Singh",
    "Abhay Pratap Singh",
    "Parmendra Singh",
    "Pummy",
    "Seema",
    "Reena",
    "Rupesh",
    "Sachin",
    "Shaily",
]

list_final = filter(lambda n: len(n) > 8, lst_employee)

print(list(list_final))