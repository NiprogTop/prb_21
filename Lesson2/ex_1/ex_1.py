"""
B. "Напитки"
https://codeforces.com/problemset/problem/200/B
"""


def percent(num, all_drin):
    full_drink = 0
    for i in all_drin:
        full_drink += int(i)
    return full_drink / num


def main():
    orange_num = int(input())
    list_menu = list(map(int, input().split()))
    print(percent(orange_num, list_menu))


if __name__ == '__main__':
    main()
