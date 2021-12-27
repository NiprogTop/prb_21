morz = {'\t': '\t', 'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}


def trans(text_inp):
    morz_text = []
    for i in text_inp:
        morz_text.append(morz.get(i, '\t'))
    return morz_text


def main():
    str_text = str(input()).lower()
    morze_text = trans(str_text)
    for i in morze_text:
        print(i, end='')


if __name__ == '__main__':
    main()
