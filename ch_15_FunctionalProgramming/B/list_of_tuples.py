nums = [10,20,30,40,50,60,70,80]
strs = ['A','B','C','D','E','F','G','h']

lst_tpl = list(map(lambda x,y : (x,y),nums,strs))

print(lst_tpl)