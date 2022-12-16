# The Lists

squares=[1, 4, 9, 16, 25]
alphabets=['a', 'b', 'c', 'd', 'e', 'f']
suckLists=[['a', 'b', 'c', 'd'], [1, 2, 3, 4]] # can nest a lists

print(squares)
print(squares[2]) # can indexed
print(squares[2:])
print(squares[:2]) # 
print(squares[:]) # returns a shallow copy of the lists
print(squares * 2) # support concatination
squares.append(50) # add item
print(squares)

alphabets[3:]=['D', 'E', 'F', 'G'] # replace item
print(alphabets)
alphabets[3:]=[] # remove item
print(alphabets)
alphabets[:]=[]
print(alphabets)

print(len(suckLists))
print(suckLists[1])
