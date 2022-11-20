fruits = ["banana", "apple", "orange", "apple", "mango"] # list

countApple = fruits.count("apple") # count item list
print(countApple)

indexMango = fruits.index("mango") # index item list
print(indexMango)

reverseFruits = fruits.reverse() # reverse list
print(fruits)

appendPear = fruits.append("pear") # append item from last list
print(fruits)

sortFruits = fruits.sort() # sort list
print(fruits)

popFruits = fruits.pop() # pop list, remove from last item or use index
print(popFruits)

print(fruits) # results of all methods
