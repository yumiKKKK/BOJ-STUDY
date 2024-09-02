def solution(phone_book):
    lens = set([len(i) for i in phone_book])
    for i in lens:
        nolen = [x[:i] for x in phone_book if len(x) != i]
        yeslen = [x[:i] for x in phone_book if len(x) == i]
        if set(nolen) & set(yeslen):
            return False
    return True