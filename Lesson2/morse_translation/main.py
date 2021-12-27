morze = {' ': ' ', 'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••', 'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••', 'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••', 'm': '——', 'n': '—•', 'o': '———', 'p': '•——•', 'q': '——•—', 'r': '•—•', 's': '•••', 't': '—', 'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—', 'y': '—•——', 'z': '——••'}


def trans(text_inp):
    mrz_text = []
    for i in text_inp:
        mrz_text.append(morze.get(i))
    return mrz_text


def main():
    str_text = str(input()).lower()
    print(*trans(str_text))


if __name__ == '__main__':
    main()
