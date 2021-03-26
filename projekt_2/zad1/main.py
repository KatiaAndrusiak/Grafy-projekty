def deg_seq(c) -> bool:
    print(' '.join(map(str, c)))
    print()
    c = sorted(c, reverse=True)
    if sum(c) % 2 == 1:
        return False
    while True:
        print(' '.join(map(str, c)))
        if all(v == 0 for v in c):
            return True
        if (c[0] < 0) or (c[0] >= len(c)) or any(v < 0 for v in c):
            return False
        for i in range(1, c[0] + 1):
            c[i] = c[i] - 1
        c[0] = 0
        c = sorted(c, reverse=True)


def read_list_from_file(file_name, mylist) -> object:
    with open(file_name) as f:
        for line in f:
            mylist = line.split()
    return mylist


degree_sequence = []
degree_sequence = read_list_from_file("degreeSeq.txt", degree_sequence)

degree_sequence = list(map(int, degree_sequence))

if deg_seq(degree_sequence):
    print("\nCiąg jest graficzny")
else:
    print("\nCiąg nie jest graficzny")
