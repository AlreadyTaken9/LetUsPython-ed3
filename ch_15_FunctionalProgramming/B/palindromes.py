lst = ["Malyalam", "Drawing", "madamlamadam", "1234321"]

lst_pal = list(filter(lambda n: (n == "".join(reversed(n))), lst))

print(lst_pal)
