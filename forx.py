c = [1, 1, -5, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def a(x: list):
    new = []
    for i in x:
        if i < 5:
            new.append(i)
        else:
            continue
    print(sorted(set(new)))
a(c)
