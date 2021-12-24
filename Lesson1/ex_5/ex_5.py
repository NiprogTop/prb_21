def G_go_top(z, i, a):  # не использовать транслит!!!
    for j in range(0, i):
        flag_B=True
        for k in range(len(a) - 1):
            if a[k] == "B" and a[k+1] == "G" and flag_B:
                flag_B = False;
                a[k] = "G"
                a[k+1] = "B"
            else:
                flag_B = True
    return print(*a, sep="")


def main():
    z, i = map(int, input().split())
    a = list(input())
    G_go_top(z, i, a)


if __name__ == '__main__':
    main()