#!/usr/bin/python3
def multiple_returns(sentence):
    slen = len(sentence)
    nt = ()
    nt = nt + (slen, )
    if sentence == "":
        fchar = None
    else:
        fchar = sentence[0]
    nt = nt + (fchar, )
    return nt
