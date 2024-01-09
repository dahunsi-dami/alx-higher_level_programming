#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        slen = len(sentence)
        nt = ()
        nt = nt + (slen, )
        fchar = sentence[0]
        nt = nt + (fchar, )
        return nt
