def counter():
    filename = input("ENter filename:")

    nowords = 0

    file = open(filename,'r')
    for line in file:
        words = line.split()
        nowords = nowords + len(words)
    print(nowords)

counter()