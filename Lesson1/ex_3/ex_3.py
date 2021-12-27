def simbol(i):
    kol = 0
    j = dict.fromkeys(i, 0)
    for c in j:
        j[c] += 1
    for h in j:
        if j[h] == 1:
            kol += 1
    print("Количество неповторяющихся символов: " + str(kol))


def main():
    word = input().lower()
    simbol(word)


if __name__ == '__main__':
    main()
