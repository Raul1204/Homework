filename = "text.txt"

fp = open(filename)
print(fp.read())
fp.close()

with open(filename) as fp:
    for line in fp:
        line = line.replace("\n","")
        print(f"Line: {line}")
