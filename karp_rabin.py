from rollinghashADT import rollinghash

def find_first(s1, s2):
    ans_str = []
    r1 = rollinghash()
    for i in s1[:len(s2)]: r1.append(i)

    r2 = rollinghash()
    for i in s2: r2.append(i)

    for i in range(len(s2), len(s1)+1):
        if r1.hashval() == r2.hashval():
            if s2 == s1[i - len(s2) : i]:
                ans_str.append(i - len(s2))
        elif i < len(s1):
            r1.append(s1[i])
            r1.pop_left(s1[i - len(s2)])
    return ans_str
