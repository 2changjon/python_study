for i in range(2, 10):
    for j in range(1, 10):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
    print('')

result = [i*j for i in range(2, 10) for j in range(1, 10)]
print(result)