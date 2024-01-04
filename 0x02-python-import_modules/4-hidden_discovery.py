#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    moddefin = dir(hidden_4)
    definlen = len(moddefin)
    for i in range(0, definlen):
        if moddefin[i][0:2] != "__":
            print(moddefin[i])
