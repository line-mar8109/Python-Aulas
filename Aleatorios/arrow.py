def arrow(n):
    for i in range(-n, n):
        if i == 0:
            print(n * 3 * "*")
        else:
            print(n * 2 * " " + (n - abs(i)) * "*")


arrow(5)
