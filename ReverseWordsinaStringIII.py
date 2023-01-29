def reverseWords(self, s: str) -> str:
    split_s = s.split(" ")

    ss = ""

    for i in split_s:
        a = [i[-j] for j in range(1, len(i) + 1)]
        ss += ''.join(a) + ' '
    return ss.rstrip()