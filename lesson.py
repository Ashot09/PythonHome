x = 'a,2,b,5,c,8,a,4,e,11'
x = x.split(",")
dict1 = {}
for i in range(0,len(x),2):
    key  = x[i]
    value = int(x[i+1])
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value
print(dict1)

