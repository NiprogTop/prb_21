"""
C. "Система регистрации"
https://codeforces.com/problemset/problem/4/C
"""


def check(num, nicknames):
    full_list = []
    for i in nicknames:
        if i in full_list:
            print(i + "1")
        else:
            full_list.append(i)
            print("OK")


def main():
    num = int(input())
    nick_list = []
    for i in range(num):
        nick_list.append(input())
    check(num, nick_list)


if __name__ == '__main__':
    main()
