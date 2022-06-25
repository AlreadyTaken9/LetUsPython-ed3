def fun1(d):
    if d['type'] == 'Dog':
        return d['Age']

    else:
        return 0

def fun2(n):
    if n==0:
        return False
    else:
        return True

dict = {
    't1' : {'Type':'Cat', 'Name':'Lilly','Age':6},
    't2' : {'Type':'Dog', 'Name':'Gabbar','Age':4},
    't3' : {'Type':'Dog', 'Name':'Kaatiya','Age':9}
}

lst = list(filter(fun2,list(map(fun1,list(dict.values())))))
print('the sum of all dogs ages : ',sum(lst)/len(lst))