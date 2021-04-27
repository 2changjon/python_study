a = 1


def vartest1():
    global a
    a += 1


vartest1()
print("vartest1", a)


def vartest2(num):
    num += 1
    return num


a = vartest2(a)
print("vartest2", a)
