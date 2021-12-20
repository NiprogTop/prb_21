def task4_solver(last_pos, port):
    pos = 0
    while pos < last_pos - 1:
        pos += port[pos]

    if pos == last_pos - 1:
        return print("YES")
    else:
        return print("No")


def main():
    z, i = map(int, input().split())
    a = list(map(int, input().split()))
    task4_solver(i, a)


if __name__ == '__main__':
    main()
