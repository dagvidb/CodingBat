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


# missing_char

def missing_char(str, n):  # Shadow built-in name warning
    return str[:n] + str[n + 1:]


print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))


# monkey_trouble

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))


# parrot_trouble

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
