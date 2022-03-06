def file_read(fname):
    with open(fname) as f:
        c = f.readlines()
    print(c)


file_read("a.txt")
