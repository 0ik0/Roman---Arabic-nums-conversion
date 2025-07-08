dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
y = input('Enter value: ')
x = list(y)

m = 0
for i in range(len(x) - 1):
    
    if dict[x[i]] >= dict[x[i + 1]]:
        m += dict[x[i]]

    else:    
        m = m - dict[x[i]]
    
    
m += dict[x[len(x) - 1]]

print(m)