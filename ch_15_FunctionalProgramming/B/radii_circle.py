lst = [1.25,3.22,4.68,10.95,32.55,12.54]

area = map(lambda n : round(n*3.14*n,2),lst)
list_area = (list(area))
print(list_area)