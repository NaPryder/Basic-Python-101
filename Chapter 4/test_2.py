

a = [1, 2, 11, 55, -99, 98, 100, 155]
x = []

for i, item in enumerate(a):
    print(i, item)
    
    if i%2 == 0:
        if item >= 0:
            x.append(item/5000)
        
        else:
            x.append('XXXX')

# List comprehension
y = [item/5000 if item>=0 else 'XXXX' for i, item in enumerate(a) if i%2 == 0]

print(x)
print(y)