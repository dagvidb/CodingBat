###############################################
# Warmup_1
###############################################

# sleep_in

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))


# diff21

def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    else:
        return abs(n - 21)


print(diff21(19))
print(diff21(10))
print(diff21(21))


# near_hundred


def near_hundred(n):
    if abs(100 - n) > 10 and abs(200 - n) > 10:
        return False
    else:
        return True


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))
