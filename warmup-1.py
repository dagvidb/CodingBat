###############################################
# Warmup_1
###############################################

# sleep_in

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# diff21

def diff21(n):
    if n > 21:
        return 2 * abs(n - 21)
    else:
        return abs(n - 21)


# near_hundred

def near_hundred(n):
    if abs(100 - n) > 10 and abs(200 - n) > 10:
        return False
    else:
        return True


# missing_char

def missing_char(str, n):  # Shadow built-in name warning
    return str[:n] + str[n + 1:]


# monkey_trouble


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


# parrot_trouble

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False


# pos_neg


def pos_neg(a, b, negative):
    if (a * b < 0) and not negative:
        return True
    elif a < 0 and b < 0 and negative:
        return True
    else:
        return False


# front_back

def front_back(str):
    n = len(str)
    if n > 1:
        return str[-1] + str[1:-1] + str[0]
    else:
        return str

    # sum_double

def sum_double(a, b):
    if a == b:
        return 4 * a
    else:
        return a + b


# makes_ten

def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


# not_string

def not_string(str):
    if str[0:3] == "not":
        return str
    else:
        return "not" + " " + str


# front3

def front3(str):
    return 3 * str[0:3]
