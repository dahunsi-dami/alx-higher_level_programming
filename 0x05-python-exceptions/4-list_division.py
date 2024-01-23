#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nu_nu_list = []
    for i in range(list_length):
        try:
            a, b = my_list_1[i], my_list_2[i]
            ans = a / b
        except ZeroDivisionError:
            ans = 0
            print("division by {}".format(ans))
        except TypeError:
            ans = 0
            print("wrong type")
        except IndexError:
            ans = 0
            print("out of range")
        finally:
            nu_nu_list.append(ans)
    return nu_nu_list
