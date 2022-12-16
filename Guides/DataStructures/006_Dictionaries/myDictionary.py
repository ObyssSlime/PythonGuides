tel = {"Jack": 1000, "Thiery": 2000}
print(tel)

tel["Harry"] = 3000 # add item from dict
print(tel)

del tel["Jack"] # delete item in dict
print(tel)

print(list(tel)) # list dict
print(sorted(tel)) # sort dict
print("Jack" in tel) # check item from dict
