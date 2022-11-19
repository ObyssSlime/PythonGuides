for x in range(5):
    print(x)

print(list(range(5, 10))) # sometimes this is called the 'step'
print(list(range(0, 10, 2)))

colors=['red', 'blue', 'green']
for x in range(len(colors)):
    print(x, colors[x])

print(sum(range(5))) # return 0+1+2+3+4
