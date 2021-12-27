def pal(i):
    if i == i[::-1]:
        print('Является палиндромом')
    else:
        print('Не является палиндромом')


def main():
    word = input().lower()
    pal(word)


if __name__ == '__main__':
    main()
