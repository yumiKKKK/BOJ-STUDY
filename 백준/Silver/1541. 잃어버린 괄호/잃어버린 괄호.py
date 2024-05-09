arr = input().split("-")
calc = 0

for i in arr[0].split('+'):
    calc += int(i)
    
for i in arr[1:]:
    for j in i.split('+'):
        calc -= int(j)
        
print(calc)