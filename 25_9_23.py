'''string concatenation
operator over loading'''
first = "rajeev"
second = "kamisetty"
print(first +" "+second)

#f'string / interpolation
first = "rajeev"
second = "kamisetty"
name = f"{first} {second}"
print(name)

# sting join method
first = "rajeev"
second = "kamisetty"
lst = (first , second)
print(" ".join(lst))

"""string split 
splict"""
date = "25 sep 2023"
print(date.split(" "))

#split by line
adress : str = """10/4
main bazar,
cumbum"""
print(adress.splitlines())

#partation
date = "25 sep 2023 09"
print(date.partition(" "))

#rpartation
date = "25 sep 2023 09"
print(date.rpartition(" "))
