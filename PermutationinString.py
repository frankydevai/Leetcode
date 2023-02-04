def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    char_count = [0] * 26
    for c in s1:
        char_count[ord(c) - ord('a')] += 1

    start, end = 0, 0
    count = len(s1)
    while end < len(s2):
        if char_count[ord(s2[end]) - ord('a')] >= 1:
            count -= 1
        char_count[ord(s2[end]) - ord('a')] -= 1
        end += 1

        if count == 0:
            return True

        if end - start == len(s1):
            if char_count[ord(s2[start]) - ord('a')] >= 0:
                count += 1
            char_count[ord(s2[start]) - ord('a')] += 1
            start += 1

    return False
