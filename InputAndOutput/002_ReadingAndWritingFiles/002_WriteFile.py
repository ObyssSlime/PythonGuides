f = open("002_Workfile.txt", "rb+")

f.write(b"0123456789abcdef")
print(f.seek(13))
print(f.read(2))
