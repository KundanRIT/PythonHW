def permutation(str, l, r):
    if l==r:
        print(str)
    else:
        for i in range(l,r):
            if str[i] not in str[i+1:]:
                str = swap(str, l, i)
                permutation(str, l+1, r)
                str = swap(str, l, i)


def swap(str, i, j):
    l = list(str)
    l[i], l[j] = l[j], l[i]
    return "".join(l)

permutation("aab",0,3)