# calculating sum if args > 0
def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0


# print(paperwork(3, 2))


# Counting positives and sum of negatives
def count_positives_sum_negatives(arr):
    return [len([i for i in arr if i > 0]), sum([i for i in arr if i < 0])] if arr else []


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# print(count_positives_sum_negatives(a))


# Impressively stupidly clever way to convert string to int
def stupid(s):
    if s == '0':
        return 0
    elif s == '1':
        return 1
    elif s == '2':
        return 2
    elif s == '3':
        return 3
    elif s == '4':
        return 4
    elif s == '5':
        return 5
    elif s == '6':
        return 6
    elif s == '7':
        return 7
    elif s == '8':
        return 8
    else:
        return 9


def string_to_number(s):
    if isinstance(s, int):
        return s
    r = 0
    for c in s:
        if c == '-':
            continue
        r = r * 10 + stupid(c)
    return r if s[0] != '-' else -1 * r


# Add to dict() and count

# fhand = open('romeo-full.txt')
counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

newlist = list()
for key, value in counts.items():
    newtup = (value, key)
    newlist.append(newtup)

newlist = sorted(newlist, reverse=True)
for val, key in newlist[0:10]:
    print(key, val)


# Count and compare characters in string. USING COUNTER BY THE WAY. And dict too
def xo(s):
    seen = {'o': 0, 'x': 0}
    for i in s.lower():
        if i == 'o' or i == 'x':
            seen[i] = seen.get(i) + 1
    return seen['o'] == seen['x']


def betterXO(s):
    s = s.lower()
    return s.count('x') == s.count('o')


# a = 'xxXooo'
# print(betterXO(a))

# Sorting only odds and leaving evens in place with iter and without
def sort_array(source_array):
    sorted_neg = (sorted((i for i in source_array if i % 2 == 1), reverse=True))
    return [x if x % 2 == 0 else sorted_neg.pop() for x in source_array]


def sort_array2(source_array):
    odds = iter(sorted(v for v in source_array if v % 2))
    return [next(odds) if i % 2 else i for i in source_array]


# a = [5, 3, 2, 8, 1, 4]
# print(sort_array(a))


# Returning list of digits of a number in reverse order
def digitize(n):
    # return [int(i) for i in list(str(n))[::-1]]
    return list(map(int, str(n)[::-1]))


# a = 78128351
# print(digitize(a))


# Fiding what position sums of both part of list of ints are equal
def find_even_index(arr):
    for index, value in enumerate(arr):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    else:
        return -1


# a = [1,2,3,4,3,2,1]
# b = [1,100,50,-51,1,1]
# c = []
#
# print(find_even_index(a))
# print(find_even_index(c))

# Returning highest scored word given that a = 1, b = 2, c = 3 and so on
def high(x):
    dct = dict()
    for i in list(x.split(' ')):
        dct[i] = sum([ord(character) - 96 for character in list(i)])
    print(dct)
    return max(dct, key=dct.get)


def better_high(x):
    return max(x.split(' '), key=lambda l: sum(ord(i) for i in l))


# a = 'aa b'
# print(high(a))

# Finding smileys!
def count_smileys(arr):
    return sum([1 if (any(eyes in [':', ';'] for eyes in x)) and (any(mouths in ['D', ')'] for mouths in x)) and (
        True if len(x) == 2 else any(noses in ['-', '~'] for noses in x)) else 0 for x in arr])


from re import findall


def better_count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))


# a = [':D',':~)',';~D',':)']
# b = [';]', ':[', ';*', ':$', ';-D']
# c = []
#
# print(count_smileys(a))
# print(count_smileys(b))
# print(count_smileys(c))

import re


# Counting number of letters o to z
def printer_error(s):
    return f"{len(re.findall('[o-z]', s))}/{len(s)}"


# s="aaaxbbbbyyhwawiwjjjwwm"
# print(printer_error(s))


# Counting points in pairs of values in str format
def points(games):
    points = 0
    games = [i.split(':') for i in games]
    for i in games:
        if i[0] > i[1]:
            points += 3
        elif i[0] == i[1]:
            points += 1
    return points


# print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))

# Counting series sum
def series_sum(n):
    myval = 0
    for idx in range(0, n):
        myval += 1 / (1 + 3 * idx)
    return "{:.2f}".format(myval)


def series_sum1(n):
    fractions = []
    for n in range(1, 3 * n - 1, 3):
        fractions.append(1 / n)
    return "{:.2f}".format(sum(fractions))


# a = 81
# print(series_sum(a))
# print(series_sum1(a))

# Looking for Eureka numbers
def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    reslist = []
    for i in range(a, b + 1):
        digitsum = 0
        for idx, character in enumerate(list(str(i))):
            digitsum += int(character) ** (idx + 1)
        if digitsum == i:
            reslist.append(i)
    return reslist


# print(sum_dig_pow(1, 200))

# Returning list of given strings with index letter capitalized
def wave(people):
    people = [people for _ in range(len(people))]
    res = []
    for idx, word in enumerate(people):
        mylst = list(word)
        if mylst[idx] != ' ':
            mylst[idx] = list(word)[idx].upper()
            res.append("".join(mylst))
    return res


def cleverwave(s):
    return [s[:i] + s[i].upper() + s[i + 1:] for i in range(len(s)) if s[i].isalpha()]


print(wave(' gap '))
print(cleverwave(' gap '))


# Reversing words in string saving all punctuation
def reverse_words(text):
    revdict = {}
    replacedlist = []
    for i in list(text.split()):
        revdict[i] = i[::-1]
    for word, replacement in revdict.items():
        if word not in replacedlist:
            print(text)
            text = text.replace(word, replacement)
        replacedlist.append(word)
    return text


# Detecting pangrams. The sucky way
def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char.lower() not in s:
            return False
    return True


# Detecting pangrams the clever way
import string


def is_pangram_but_better(s):
    return set(string.ascii_lowercase).issubset(s.lower())


print(is_pangram('TThis isnt a pangram'))
print(is_pangram_but_better('The quick brown fox jumps over the lazy dog'))


def correctreversewords(text):
    return ' '.join([i[::-1] for i in text.split(' ')])


# print(correctreversewords("stressed     desserts"))


# Traffic lights
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]


# Counting sheep
def count_sheep(n):
    return ''.join(f'{i} sheep...' for i in range(1, n + 1))


# Returning list with max repetitions
def delete_nth(order, max_e):
    order = order[::-1]
    for i in order:
        while order.count(i) > max_e:
            order.remove(i)
    return order[::-1]


def delete_nth_with_new_arr(order, max_e):
    lst = []
    for i in order:
        if lst.count(i) < max_e:
            lst.append(i)
    return lst


# print(delete_nth_with_new_arr([1, 1, 3, 3, 7, 2, 2, 2, 2], 2))
# print([1, 1, 3, 3, 7, 2, 2, 2])

# Breaking camel case
def solution(s):
    lst = list(s)
    for idx, val in enumerate(lst):
        if lst[idx - 1] != ' ' and val.isupper():
            lst.insert(idx, ' ')
    return ''.join(lst)


def better_solution(s):
    return ''.join(' ' + char if char.isupper() else char for char in s)


#
# print(better_solution("breakCamelCase"))

# Getting grade
def get_grade(s1, s2, s3):
    res = (s1 + s2 + s3) / 3
    print(res)
    if 90 <= res <= 100:
        return 'A'
    elif 80 <= res < 90:
        return 'B'
    elif 70 <= res < 80:
        return 'C'
    elif 60 <= res < 70:
        return 'D'
    elif 0 <= res < 60:
        return 'F'


#
# print(get_grade(95, 90, 93))

# Searching for Eureka
def dig_pow(n, p):
    mysum = sum(int(i) ** int(pow) for i, pow in zip(list(str(n)), list(range(p, p + len(list(str(n)))))))
    if mysum % n == 0:
        return int(mysum / n)
    else:
        return -1


def btrdig_pow(n, p):
    mysum = 0
    for idx, val in enumerate(str(n)):
        mysum += pow(int(val), idx + p)
    if mysum % n == 0:
        return mysum / n
    else:
        return -1


# print(btrdig_pow(89, 1))
# print(dig_pow(46288, 3))

# Searching for eureka in a range
def sum_dig_pow(a, b):  # range(a, b + 1) will be studied by the function
    reslist = []
    for i in range(a, b + 1):
        digitsum = 0
        for idx, character in enumerate(list(str(i))):
            digitsum += int(character) ** (idx + 1)
        if digitsum == i:
            reslist.append(i)
    return reslist


# Return tribonacci sequence
def tribonacci(signature, n):
    for i in range(0, n):
        signature.append(sum(signature[-3:]))
    return signature[:n]


# print(tribonacci([1, 1, 1], 10))


# Building towers of *
def tower_builder(n_floors):
    return [(' ' * (n_floors - i)) + ('*' + ('*' * (2 * (i - 1)))) + (' ' * (n_floors - i)) for i in
            range(1, n_floors + 1)]


# print(tower_builder(7))
# tower = [
#     "     *     ",
#     "    ***    ",
#     "   *****   ",
#     "  *******  ",
#     " ********* ",
#     "***********"
# ]


# Squaring digits in a number
def square_digits(num):
    return int(''.join([str(int(i) * int(i)) for i in str(num)]))


#
# print(square_digits(9119))

# Counting population
def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = int(p0 + (p0 * (percent / 100)) + aug)
        print(p0)
        year += 1
    return year


# print(nb_year(1000, 2.0, 50, 1214))

# Greets
def greet(language):
    translation = {'english': 'Welcome',
                   'czech': 'Vitejte',
                   'danish': 'Velkomst',
                   'dutch': 'Welkom',
                   'estonian': 'Tere tulemast',
                   'finnish': 'Tervetuloa',
                   'flemish': 'Welgekomen',
                   'french': 'Bienvenue',
                   'german': 'Willkommen',
                   'irish': 'Failte',
                   'italian': 'Benvenuto',
                   'latvian': 'Gaidits',
                   'lithuanian': 'Laukiamas',
                   'polish': 'Witamy',
                   'spanish': 'Bienvenido',
                   'swedish': 'Valkommen',
                   'welsh': 'Croeso'
                   }
    return translation.get(language, 'Welcome')


# print(greet('atch'))

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"


# Calculator
def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')


def human_years_cat_years_dog_years(human_years):
    cat = dog = 15
    if human_years == 2:
        return [human_years, cat + 9, dog + 9]
    elif human_years >= 3:
        cat += 9
        dog += 9
        for i in range(1, human_years - 1):
            print(cat)
            cat += 4
            dog += 5
    return [human_years, cat, dog]


# print(human_years_cat_years_dog_years(10))

# Cat Years
#
#     15 cat years for first year
#     +9 cat years for second year
#     +4 cat years for each year after that
#
# Dog Years
#
#     15 dog years for first year
#     +9 dog years for second year
#     +5 dog years for each year after that


def high_and_low(numbers):
    lst = [int(i) for i in numbers.split(' ')]
    return f'{max(lst)} {min(lst)}'


# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))


def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


# print(longest("aretheyhere", "yestheyarehere"))
# print(longest("loopingisfunbutdangerous", "lessdangerousthancoding"))


def nb_dig(n, d):
    print([str(i ** 2) for i in range(1, n + 1)])
    print(''.join(str(i ** 2) for i in range(1, n + 1)))

    return ''.join(str(i ** 2) for i in range(0, n + 1)).count(str(d))


# print(nb_dig(5750, 0))

# Correct for 5 1 0 in uppercase str
def correct(s):
    return s.replace('5', 'S').replace('0', 'O').replace('1', 'I')


import string


# Rot cypher. Or ceasar cypher
def rot13(message):
    lwrc = string.ascii_lowercase
    uprc = string.ascii_uppercase
    res = []
    for i in message:
        if i in lwrc:
            i = lwrc[(lwrc.index(i) + 13) % 26]
        elif i in uprc:
            i = uprc[(uprc.index(i) + 13) % 26]
        res.append(i)
    return ''.join(res)


# print(rot13('teStzz'))

# String manipulation
def accum(s):
    return '-'.join((val * (idx + 1)).title() for idx, val in enumerate(list(s)))


# print(accum('message'))


def queue_time1(customers, n):
    registers = [0] * n
    customers = customers[::-1]
    time = 0
    if n > len(customers):
        return max(customers)
    while len(customers) > 0:
        if min(registers) == 0:
            for idx, val in enumerate(registers):
                if registers[idx] == 0 and len(customers) > 0:
                    registers[idx] = customers.pop()
        while min(registers) > 0:
            registers = [i - 1 for i in registers]
            time += 1
    return time + max(registers)


def queue_time2(customers, n):
    registers = customers[:n]
    customers = customers[:n - 1:-1]
    while len(customers) > 0:
        registers = [i + customers.pop() if i == min(registers) and len(customers) > 0 else i for i in registers]
    return max(registers, default=0)


def queue_time(customers, n):
    registers = [0] * n
    for i in customers:
        registers[registers.index(min(registers))] += i
    return max(registers)


# print(queue_time([24, 26, 44, 28, 26, 16, 25, 8, 19, 47, 5, 23, 17, 11, 30, 49, 32, 19, 35, 50, 22, 31, 37, 13, 15, 44, 46, 11, 4, 14, 23, 5, 5, 39, 34, 45, 3, 13, 19, 31, 35, 7, 12, 33, 48, 35, 9, 45, 32, 18, 15, 7, 12, 34, 13, 26, 18, 43, 47, 48, 27, 18, 32, 43, 29, 8, 50, 22, 25, 27, 28, 14, 13, 20, 50, 15, 6, 23, 22, 8, 41, 24, 38, 28, 8, 13, 33, 18, 35, 43, 2, 42, 16, 9, 12, 5, 47, 10, 14, 29, 18, 23, 15, 32, 20, 38, 45, 2, 31, 9, 36, 8, 12, 11, 15, 46, 32, 19, 11, 48, 22, 25, 8, 27, 4, 20, 29, 5, 49, 15, 38, 30, 5, 36, 34, 35, 30, 45, 20, 1, 49, 48, 15, 29, 5, 48, 22, 48, 49, 20, 27, 33, 20, 16, 17, 2, 2, 28, 39, 16, 33, 9, 31, 13, 12], 32))
# print(queue_time2([24, 26, 44, 28, 26, 16, 25, 8, 19, 47, 5, 23, 17, 11, 30, 49, 32, 19, 35, 50, 22, 31, 37, 13, 15, 44, 46, 11, 4, 14, 23, 5, 5, 39, 34, 45, 3, 13, 19, 31, 35, 7, 12, 33, 48, 35, 9, 45, 32, 18, 15, 7, 12, 34, 13, 26, 18, 43, 47, 48, 27, 18, 32, 43, 29, 8, 50, 22, 25, 27, 28, 14, 13, 20, 50, 15, 6, 23, 22, 8, 41, 24, 38, 28, 8, 13, 33, 18, 35, 43, 2, 42, 16, 9, 12, 5, 47, 10, 14, 29, 18, 23, 15, 32, 20, 38, 45, 2, 31, 9, 36, 8, 12, 11, 15, 46, 32, 19, 11, 48, 22, 25, 8, 27, 4, 20, 29, 5, 49, 15, 38, 30, 5, 36, 34, 35, 30, 45, 20, 1, 49, 48, 15, 29, 5, 48, 22, 48, 49, 20, 27, 33, 20, 16, 17, 2, 2, 28, 39, 16, 33, 9, 31, 13, 12], 32))
# print(queue_time1([24, 26, 44, 28, 26, 16, 25, 8, 19, 47, 5, 23, 17, 11, 30, 49, 32, 19, 35, 50, 22, 31, 37, 13, 15, 44, 46, 11, 4, 14, 23, 5, 5, 39, 34, 45, 3, 13, 19, 31, 35, 7, 12, 33, 48, 35, 9, 45, 32, 18, 15, 7, 12, 34, 13, 26, 18, 43, 47, 48, 27, 18, 32, 43, 29, 8, 50, 22, 25, 27, 28, 14, 13, 20, 50, 15, 6, 23, 22, 8, 41, 24, 38, 28, 8, 13, 33, 18, 35, 43, 2, 42, 16, 9, 12, 5, 47, 10, 14, 29, 18, 23, 15, 32, 20, 38, 45, 2, 31, 9, 36, 8, 12, 11, 15, 46, 32, 19, 11, 48, 22, 25, 8, 27, 4, 20, 29, 5, 49, 15, 38, 30, 5, 36, 34, 35, 30, 45, 20, 1, 49, 48, 15, 29, 5, 48, 22, 48, 49, 20, 27, 33, 20, 16, 17, 2, 2, 28, 39, 16, 33, 9, 31, 13, 12], 32))


# Extract domain names with regex
def domain_name(url):
    from re import findall, VERBOSE

    try:
        url = findall("""\A
                        (?: http
                        s?
                        ://)?         # matches http:// or https:// or nothing

                        (?: www.)?    # matches www. or nothing

                        ([- a-z]+)    # matches a sequence of letters and dashes

                        (?: .com|.ru)     # matches either .com or .ru
                        (?: [/ a-z]+)?    # matches a sequence or letters and slashes
                        \Z""", url, VERBOSE)
        return url[0]
    except:
        return "Invalid URL."


def domain_name2(url):
    regex = r"(?:https?://)?(www\.)?([a-zA-Z0-9_-]+)(\.[a-zA-Z0-9.-]+)"
    return list(re.findall(regex, url)[0])[1]


# Calculator
def arithmetic(a, b, operator):
    match operator:
        case 'add':
            operator = '+'
        case 'substract':
            operator = '-'
        case 'multiply':
            operator = '*'
        case 'divide':
            operator = '/'
        case _:
            return 'Wrong operator'
    return eval(f'{a}{operator}{b}')


# print(arithmetic(4, 8, 'aadd'))


def DNA_strand(dna):
    s = ''
    for i in dna:
        if i == 'A':
            s += 'T'
        elif i == 'T':
            s += 'A'
        elif i == 'G':
            s += 'C'
        elif i == 'C':
            s += 'G'
    return s


# print(DNA_strand('ATTGC'))


# Translating string
def DNA_strand1(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


# print(DNA_strand1('ATTGC'))


# Sort array by length
def sort_by_length(arr):
    return sorted(arr, key=len)


def stray3(arr):
    s = list(set(arr))
    if arr.count(s[0]) > 1:
        return s[1]
    else:
        return s[0]


def stray2(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i


def stray1(arr):
    return min(arr, key=arr.count)


# print(stray1([2, 3, 2, 2, 2]))

# Fiding middle
def gimme(input_array):
    for i in input_array:
        if min(input_array) < i < max(input_array):
            return input_array.index(i)


# Finging smallest word by length and returning it's length
def find_short(s):
    return len(sorted(s.split(), key=len)[0])


# Capitalizing and lowering in sting
def title_case1(title, minor_words=''):
    title = title.lower()
    s = []
    for i in title.split():
        if i not in minor_words.split():
            s.append(i.title())
        else:
            s.append(i)
    s[0] = s[0].title()
    return " ".join(s)


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join(word if word in minor_words else word.capitalize() for word in title)


# print(title_case('a clash of KINGS', 'a an the of'))

# Lambda calc

def zero(op=None): return op(0) if op else 0


def one(op=None): return op(1) if op else 1


def two(op=None): return op(2) if op else 2


def three(op=None): return op(3) if op else 3


def four(op=None): return op(4) if op else 4


def five(op=None): return op(5) if op else 5


def six(op=None): return op(6) if op else 6


def seven(op=None): return op(7) if op else 7


def eight(op=None): return op(8) if op else 8


def nine(op=None): return op(9) if op else 9


def plus(num): return lambda x: x + num


def minus(num): return lambda x: x - num


def times(num): return lambda x: x * num


def divided_by(num): return lambda x: x / num


# print(five(times(six())))
# Out of control lambdas
id_ = lambda x: x
number = lambda x: lambda f=id_: f(x)
zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
plus = lambda x: lambda y: y + x
minus = lambda x: lambda y: y - x
times = lambda x: lambda y: y * x
divided_by = lambda x: lambda y: y / x


# If you are not familiar with a concept of 'closures' I would highly recommend you to read about it.
#
# Let's use six(times(four())) as an example. First four() is executed. To understand what's going to happened, let's try to reverse how four was created:
#
# four = number(4) => (lambda x: lambda f=id_: f(x))(4) => (lambda 4: lambda f=id_: f(4)) =>
# four = lambda f=id_: f(4)
#
# So now if we call four() without parameters, the default value for f will be used:
#
# four() => lambda f=id_: f(4) => id_(4)
#
# Since id_ = lambda x: x, it means that it will just return the argument it was passed, thus:
#
# id_(4) => 4
#
# So now we have six(times(4)). The next function to be executed will be times(4).
#
# times = lambda x: lambda y: y * x =>
# times(4) = lambda 4: lambda y: y * 4 =>
# lambda y: y * 4
#
# Basically times(4) will return a function that will be expecting an argument that will be multiplied by 4. We get to six(lambda y: y * 4), where six is:
#
# six = number(6) => (lambda 6: lambda f=id_: f(6)) => lambda f=id_: f(6) =>
# six = lambda f=id_: f(6)
#
# Because we pass a function as an argument, instead of using the default value id_, it will use the passed function:
#
# six(lambda y: y * 4) => (lambda f=id_: f(6))(lambda y: y * 4) =>
# (lambda y: y * 4)(6) =>
# lambda 6: 6 * 4 => 6 * 4 => 24
#
# As said above, the passed function will be called with 6 as an argument, and will produce 24.
#
# The rest of the stuff is easy to figure out, as long as you understand how map, variable unpacking and closure work, and that function can accept functions as arguments and return functions that later can be executed. If you still don't understand how it works, and you can see that the consepts I listed are unfamilliar, try to google them, and it should help you.
#
# I hope, my explanation was helpful.

# Getting middle letter of a word
def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 else s[len(s) // 2 - 1] + s[len(s) // 2]


# print(get_middle("test"))
# print(get_middle("testing"))

# Clever elevator conversion
def get_real_floor(n):
    return n - (n > 0) - (n > 13)


# Max result
def expression_matter(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))


# Alphabet position, it's not complex
def alphabet_position(text):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(alph.index(i) + 1) for i in text.lower() if i.isalpha()])


# print(alphabet_position("The sunset sets at twelve o' clock."))

# Multiply to the next five
def round_to_next5(n):
    return n + (5 - n) % 5


# Calculating fighter who wins first in a fight
def declare_winner(fighter1, fighter2, first_attacker):
    wrf1 = fighter2.health / fighter1.damage_per_attack
    wrf1 = wrf1 + (1 - wrf1) % 1
    wrf2 = fighter1.health / fighter2.damage_per_attack
    wrf2 = wrf2 + (1 - wrf2) % 1
    if wrf1 < wrf2:
        return fighter1.name
    elif wrf1 > wrf2:
        return fighter2.name
    elif wrf1 == wrf2:
        return first_attacker


# Better pythonic way
def declare_winner_but_better(fighter1, fighter2, first_attacker):
    cur, opp = (fighter1, fighter2) if fighter1.name == first_attacker else (fighter2, fighter1)
    while cur.health > 0:
        opp.health -= cur.damage_per_attack
        cur, opp = opp, cur
    return opp.name


# Finding mulitples up to
def find_multiples(integer, limit):
    return list(range(integer, limit + 1, integer))


# Finding n^3 + (n + 1)^3...

def find_nb1(m):
    num = (-1 + (1 + 8 * m ** 0.5) ** 0.5) / 2
    t = sum([i ** 3 for i in range(1, int(num) + 1)])
    return -1 if t != m else num


def find_nb(m):
    i = 1
    res = 0
    while res < m:
        res += i ** 3
        if res == m:
            return i
        i += 1
    return -1


def rps(p1, p2):
    if p1 == 'paper' and p2 == 'rock' or p1 == 'rock' and p2 == 'scissors' or p1 == 'scissors' and p2 == 'paper':
        return 'Player 1 won!'
    elif p2 == 'paper' and p1 == 'rock' or p2 == 'rock' and p1 == 'scissors' or p2 == 'scissors' and p1 == 'paper':
        return 'Player 2 won!'
    else:
        return 'Draw!'


def capitals(word):
    return [idx for idx, char in enumerate(word) if char.isupper()]


# print(capitals('kjfaIOASJDAKSdijASKdjIskLIAm'))

# Kadane algo
def max_sequence(arr):
    best_sum = arr[0]
    current_sum = arr[0]
    for x in arr:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum


# print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

def factorial(n):
    if 0 <= n <= 12:
        return 1 if n == 1 else n * factorial(n - 1)
    else:
        raise ValueError


# print(factorial(5))

# Check exams
def check_exam(arr1, arr2):
    return max(0, sum(4 if a == b else -1 for a, b in zip(arr1, arr2) if b))


# Sheep easy
def warn_the_sheep(queue):
    queue = queue[::-1]
    if queue[0] == 'wolf':
        return 'Pls go away and stop eating my sheep'
    else:
        return f'Oi! Sheep number {queue.index("wolf") + 1}! You are about to be eaten by a wolf!'


# Encoding word
def duplicate_encode(word):
    return ''.join('(' if word.lower().count(i.lower()) == 1 else ')' for i in word)


# Doing diamond bitches!
def diamond(n):
    if n > 0 and n % 2:
        e = n // 2 + 1
        arr = [(' ' * (e - i)) + ('*' * ((i * 2) - 1)) + '\n' for i in range(1, e + 1)]
        low = arr[:-1]
        return ''.join(arr) + ''.join(reversed(low))
    else:
        return None


print(diamond(9))


# Fib
def rfib(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = rfib(n - 1, memo) + rfib(n - 2, memo)
    print(n)
    print(memo)
    return memo[n]


# print(rfib(8))

def lfib(n):
    arr = [0, 1]
    if 0 < n < 2:
        return arr
    while len(arr) < n:
        arr.append(arr[-1] + arr[-2])
    return arr


def productFib(prod):
    arr = [0, 1]
    while (arr[-1] * arr[-2]) < prod:
        arr.append(arr[-1] + arr[-2])
    return [arr[-2], arr[-1], prod == arr[-2] * arr[-1]]


# print(productFib(714))


def betterproductFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]


# print(betterproductFib(47187234123353))

# print(lfib(50))

# Revert or rotate
def rev_rot(strng, sz):
    fs = ''
    if sz > 0:
        while len(strng) >= sz:
            chunk = strng[:sz]
            if sum(int(i) ** 3 for i in chunk) % 2:
                fs += chunk[1:] + chunk[0]
            else:
                fs += chunk[::-1]
            strng = strng[sz:]
    return fs


def first_non_consecutive(arr):
    prev = arr[0]
    for i in arr[1:]:
        if i != prev + 1:
            return i
        prev = i
    return None


# print(first_non_consecutive([1,2,3,4,6,7,8]))
# print(first_non_consecutive([1,2,3,4,5,6,7,8]))

import time


def timing(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2 - time1) * 1000.0))

        return ret

    return wrap


@timing
def prime_factors(n):
    if checkprime(n):
        return f"({n})"
    else:
        primes = []
        curr = n
        s = ''
        for num in range(2, int(n ** 0.5)):
            if checkprime(num):
                primes.append(num)
        for prime in primes:
            if curr % prime == 0:
                power = 1
                while curr % prime == 0:
                    curr /= prime
                    power += 1
                if power > 1:
                    s += f"({prime}**{power})"
                elif power == 1:
                    s += f"({prime})"
        if checkprime(curr) and curr > 2:
            s += f"({int(curr)})"
            curr /= curr
        if curr > 2:
            return f"({n})"
        return s


def checkprime(n):
    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            return False
    return True


@timing
def rf_prime_factors(n):
    s = ''
    for factor in range(2, int(n ** 0.5) + 1):
        if n % factor == 0:
            pow = 0
            while n % factor == 0:
                n /= factor
                pow += 1
            if pow > 1:
                s += f"({factor}**{pow})"
            elif pow == 1:
                s += f"({factor})"
    if n > 2:
        return s + f"({int(n)})"
    return s


# print(prime_factors(6649728829 * 7))

from math import sqrt


def bmultipliers(n):
    res = [i * i for i in range(1, int(sqrt(n + 1))) if n % i == 0]
    for f in res[1:]:
        res.append(int(n / f))
    res.append(n)
    return sorted(res)


def list_squared(m, n):
    res = []
    for i in range(m, n + 1):
        fac = [f for f in range(1, (int(sqrt(i) + 1))) if i % f == 0]
        for f in fac[1:]:
            fac.append(int(i / f))
        fac.append(i)
        print(fac)
        fsum = sum([x * x for x in set(fac)])
        print(fsum)
        if sqrt(fsum) % 1 == 0:
            res.append([i, fsum])
    return res


def multipliers(n):
    arr = [i ** 2 for i in range(1, int((n + 2) / 2)) if n % i == 0]
    arr.append(n * n)
    return arr


def race(v1, v2, g):
    if v2 < v1:
        return None
    ts = int((g * 3600) / (v2 - v1))
    minutes, seconds = divmod(ts, 60)
    hours, minutes = divmod(minutes, 60)
    return [hours, minutes, seconds]


#
# print(race(720, 850, 70))
# print([0, 32, 18])
# print(race(80, 91, 37))
# print([3, 21, 49])
# print(race(820, 81, 550))
# print(None)


def mxdiflg1(a1, a2):
    if a1 and a2:
        lmax = 0
        for i in a1:
            for j in a2:
                lmax = max(lmax, abs(len(i) - len(j)))
        return lmax
    else:
        return -1


def mxdiflg4(a1, a2):
    if a1 and a1:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1


def mxdiflg3(a1, a2):
    if a1 and a2:
        return max(abs(len(x) - len(y)) for x in a1 for y in a2)
    return -1


def mxdiflg(a1, a2):
    if a1 and a2:
        return max(len(max(a1, key=len)) - len(min(a2, key=len)),
                   len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1


# s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# print(mxdiflg(s1, s2))


def flatten_and_sort(array):
    return sorted([number for subarray in array for number in subarray])


# print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))


def bin_to_decimal(inp):
    return sum(int(val) * (2 ** (len(str(inp)) - idx - 1)) for idx, val in enumerate(str(inp)))


# print(len(max(['asd','','dasd', '132fuhoIUfh7ef7h'], key=len)))


def decrypt(encrypted_text, n):
    if n < 1:
        return encrypted_text
    if encrypted_text is None:
        return ''
    rng = int(len(encrypted_text) / 2)
    while n > 0:
        fh = encrypted_text[:rng]
        sh = encrypted_text[rng:]
        encrypted_text = ''.join(map(lambda i, j: i + j, sh, fh))
        if len(sh) != len(fh):
            encrypted_text += sh[-1]
        n -= 1
    return encrypted_text


def encrypt(text, n):
    if n < 1:
        return text
    if text is None:
        return ''
    while n > 0:
        odds = text[0::2]
        evens = text[1::2]
        text = evens + odds
        n -= 1
    return text


# print(encrypt("This is a test!", 1))
# print(decrypt("hskt svr neetn!Ti aai eyitrsig", 1))


def encrypt_this(text):
    arr = text.split()
    return ' '.join([str(ord(i[0])) + i[-1] + i[2:-1] + i[1] for i in arr])


# print(encrypt_this("Hello you asshole"))

def two_sum(numbers, target):
    res = []
    for idx, a in enumerate(numbers):
        for b in numbers[idx + 1:]:
            if a + b == target:
                res.append(numbers.index(a))
                numbers[numbers.index(a)] = None
                res.append(numbers.index(b))
                return res


# print(two_sum([1234,5678,9012], 14690))


def distinct(seq):
    return sorted(set(seq), key=seq.index)


# Convert to float with two decimal places
def two_decimal_places(n):
    return float("{:.2f}".format(n))


def two_decimal_places(n):
    return round(n, 2)


# Points on the line solution I guess

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        L = len(points)
        ans = 1
        for i in range(L):
            for j in range(i + 1, L):
                a, b = points[i], points[j]
                tmp = sum(map(lambda x:
                              (a[1] - b[1]) * (b[0] - x[0]) == (b[1] - x[1]) * (a[0] - b[0]),
                              points))
                ans = max(ans, tmp)
        return ans


# Multiplication table of the size n

def multiplication_table(size):
    res = []
    for i in range(1, size + 1):
        res.append([x * i for x in range(1, size + 1)])
    return res


#
# print(multiplication_table(3))
# print('[[1,2,3],[2,4,6],[3,6,9]]')

# Binary array to its int
def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)


# Thirtiens modulo
def thirt(n):
    powermods = [(10 ** i) % 13 for i in range(len(str(n)))]
    res = []
    while res.count(n) < 2:
        n = sum(map(lambda x, y: int(x) * int(y), powermods, str(n)[::-1]))
        res.append(n)
    return res[-1]


# Largest consecutive string
def longest_consec(strarr, k):
    if 0 < k <= len(strarr):
        res = []
        for i in range(len(strarr) - k + 1):
            res.append(''.join(strarr[i: i + k]))
        return max(res, key=len)
    else:
        return ''


def better_longest_consec(strarr, k):
    res = ''
    if 0 < k <= len(strarr):
        for i in range(len(strarr) - k + 1):
            candidate = ''.join(strarr[i: i + k])
            res = max(candidate, res, key=len)
    return res


def sum_of_differences(arr):
    arr.sort(reverse=True)
    return sum(map(lambda x, y: x - y, arr, arr[1::]))


def better_sum_of_diff(arr):
    return max(arr) - min(arr)


# print(sum_of_differences([8, 5, 4, 3, 15, 20]))
# print(better_sum_of_diff([8, 5, 4, 3, 15, 20]))


def stock_list(listOfArt, listOfCat):
    if listOfArt and listOfCat:
        resdict = {key: 0 for key in listOfCat}
        for i in listOfArt:
            if i[0] in resdict:
                resdict[i[0]] = resdict.get(i[0]) + int(''.join([num for num in i if num.isnumeric()]))
        reslist = [f'({key} : {val})' for key, val in resdict.items()]
        return ' - '.join(reslist)
    else:
        return ''


# print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B", "C", "D"]))

# print("(A : 0) - (B : 1290) - (C : 515) - (D : 600)")


def nbMonths(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    mon = 0
    lo = start_price_new - start_price_old
    savings = saving_per_month
    while lo > 0:
        mon += 1
        if mon % 2 == 0:
            percent_loss_by_month += .5
        start_price_old -= (start_price_old / 100) * percent_loss_by_month
        start_price_new -= (start_price_new / 100) * percent_loss_by_month
        lo = start_price_new - start_price_old - savings
        savings += saving_per_month
    return [mon, abs(int(lo))]


# print(nbMonths(2000, 8000, 1000, 1.5))


def convert_fracts(lst):
    den = math.lcm(*[i[1] for i in lst])
    return [[int((den / i[1])) * i[0], den] for i in lst]


import math


def convertFracts(lst):
    D = 1
    for _, d in lst:
        D *= d // math.gcd(d, D)
    return [[D * n // d, D] for n, d in lst]


# Easy translation with strings

code = 'aeiou'
trans = '12345'


def encode(st):
    translation = st.maketrans(code, trans)
    return st.translate(translation)


def decode(st):
    translation = st.maketrans(trans, code)
    return st.translate(translation)

# Iterating over list finding delta between current and next value

def gps(s, x):
    delta = []
    for i in range(1, len(x)):
        delta.append(((x[i] - x[i - 1]) * 3600) / s)
    return int(max(delta))

def gps_with_zip(s, x):
    return max([(n-m)*3600/s for (m,n) in zip(x,x[1:])])

# Best sum of k-size subarray in array

from itertools import combinations

def choose_best_sum(t, k, ls):
    return max([sum(i) for i in combinations(ls, k) if sum(i) <= t], default=None)

# # print(choose_best_sum(230, 3, [91, 74, 73, 85, 73, 81, 87]))
# ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print(choose_best_sum(230, 4, ls))
# print(choose_best_sum(430, 8, ls))



# Datetime challenge, parsing correct time and testing it
from datetime import datetime

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code is correct_code:
        return datetime.strptime(current_date, '%B %d, %Y') <= datetime.strptime(expiration_date, '%B %d, %Y')
    return False


#print(check_coupon('123','123','September 5, 2014','October 1, 2014'))

# Fibonacci but for given sig and size

def Xbonacci(signature,n):
    xbo = len(signature)
    for i in range(xbo, n):
        signature.append(sum(signature[-xbo:]))
    return signature


# print(Xbonacci([1,0,0,0,0,0,1],10),[1,0,0,0,0,0,1,2,3,6])
# print(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])

# Sorting words in sentence according to the numbers inside every word
def order(sentence):
    res = sentence.split(' ')
    res.sort(key=lambda x: [i for i in x if i.isnumeric()])
    return " ".join(res)

def order1(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))

# print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
# print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")


# Checking two strings and how many letters there are
def mix2(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
            print(hist[ch])
    print(hist)
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

def mix1(s1, s2):
    dct1 = {}
    dct2 = {}
    res = []
    for letter in s1:
        if letter.islower():
            dct1[letter] = dct1.get(letter, 0) + 1
    for letter in s2:
        if letter.islower():
            dct2[letter] = dct2.get(letter, 0) + 1
    commons = set(dct1) & set(dct2)
    uncomd2 = {i: dct2[i] for i in set(dct2) - set(dct1)}
    uncomd1 = {i: dct1[i] for i in set(dct1) - set(dct2)}
    for key in commons:
        if dct1[key] > 1 or dct2[key] > 1:
            if dct1[key] == dct2[key]:
                res.append(f'=:{key * dct1.get(key)}')
            else:
                mval = lambda: 1 if dct1[key] > dct2[key] else 2
                res.append(f'{mval()}:{key * max(dct1[key], dct2[key])}')
    if uncomd1:
        for key, value in uncomd1.items():
            if uncomd1[key] > 1:
                res.append(f'1:{key * value}')
    if uncomd2:
        for key, value in uncomd2.items():
            if uncomd2[key] > 1:
                res.append(f'2:{key * value}')
    res.sort()
    res.sort(key=lambda k: len(k) * -1)
    return "/".join(res)


def mix(s1, s2):
    res = {}
    for ch in 'abcdefghijklmnopqrstuvwxyz':
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            descriptor = '1' if val1 > val2 else '2' if val1 < val2 else '='
            res[ch] = (-max(val1, val2), f'{descriptor}:{ch * max(val1, val2)}')
    print(res)
    return '/'.join(res[ch][1] for ch in sorted(res, key=lambda x: res[x][0]))

# print(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
# print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')


#Operator as argument in input
def vert_mirror(strng):
    return [i[::-1] for i in strng]
def hor_mirror(strng):
    return strng[::-1]
# def oper(fct, s):
#     arr = s.split('\n')
#     return '\n'.join(eval("fct(arr)"))
def oper(fct, s):
    return '\n'.join(fct(s.split('\n')))
# print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
# print("QHdgSh\noaMDnH\nXxNNlC\nHxxvRi\nAvVTqb\nuRySvw")
# print(oper(hor_mirror, "lVHt\nJVhv\nCSbg\nyeCt"))
# print("yeCt\nCSbg\nJVhv\nlVHt")

# Check input type
def cookie(x):
    if not isinstance(x, bool) and isinstance(x, (int, float)):
        name = 'Monica'
    elif isinstance(x, str):
        name = 'Zach'
    else:
        name = 'the dog'
    return f'Who ate the last cookie? It was {name}!'

def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

def cookie(x):
    return f'Who ate the last cookie? It was { {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")}!'

#print(cookie('ak'))
#print(cookie(True))


# Iterating over lists of ints in list and making string out of it
def to_csv_text(array):
    res = []
    for i in array:
        res.append(','.join(map(str, i)))
    return '\n'.join(res)


# Finding out if number is divisible by 7
def seven1(m):
    s = str(m)
    i = 0
    while len(s) > 2:
        i += 1
        marr = list(s)
        head = int(''.join(marr[:-1]))
        tail = int(marr[-1])
        s = str(head - 2 * tail)
    return (int(s), i)


def seven(m, step=0):
    if m < 100: return m, step
    a, b, step = m // 10, m % 10, step + 1
    m = a - 2 * b
    return seven(m, step)

#
# print(seven(1603), (7, 2))
# print(seven(483595), (28, 4))


# Check for anagrams given word and words array
def anagrams(word, words):
    res = []
    for candidate in words:
        count = 0
        for letter in word:
            if word.count(letter) == candidate.count(letter):
                count += 1
        if count == len(word):
            res.append(candidate)
    return res

def cleveranagrams(word, words):
    return [i for i in words if sorted(i) == sorted(word)]


#print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
#print(anagrams('abba', ['abcd']), ['aabb', 'bbaa'])

def digital_root(n):
    if n < 10: return n
    return digital_root(sum(int(i) for i in str(n)))


#print(digital_root(493193))


# Hex converter

def rgb(r, g, b):
    res = ''
    for i in (r, g, b):
        if i > 255:
            i = 255
        elif i < 0:
            i = 0
        res += f'{i:02x}'
    return res


#print(rgb(1, -275, 3))


# Stripping comments with given markers
def strip_comments(strng, markers):
    res = []
    for line in strng.split('\n'):
        for mark in markers:
            if mark in line:
                line = line[:line.index(mark)]
        res.append(line)
    return '\n'.join(res)


# Button phone presses for SMS
def presses(phrase):
    abc = 'abcdefghijklmnopqrtuvwxy '
    presses = 0
    for i in phrase:
        if i.lower() == 's' or i.lower() == 'z':
            presses += 4
        elif i == 0:
            presses += 2
        elif i == '#' or i == '*':
            presses += 1
        elif i.isnumeric():
            presses += 4
        else:
            presses += abc.index(i.lower()) % 3 + 1
    return presses

#print(presses('Z0rGG'))


import random
import time

def chance_game(rounds):
    stays = []
    changes = []
    meanstays = 0
    meanchanges = 0
    for i in range(rounds):
        doors = [False] * 3
        doors[random.randint(0, 2)] = True
        player_choice = random.randint(0, 2)
        if doors[player_choice]:
            stays.append(True)
            changes.append(False)
        else:
            stays.append(False)
            changes.append(True)
        meanstays = 100 * stays.count(True) / len(stays)
        meanchanges = 100 * changes.count(True) / len(changes)
        print(f'Number of wins: {meanstays:.2f}% while staying and {meanchanges:.2f}% while changing in {i} games')
        #time.sleep(0.001)
    print(
        f'Final score: \nNumber of wins while staying: {meanstays:.2f}%\nNumber of wins while changing: {meanchanges:.2f}%\nNumber of games: {rounds}')


#chance_game(100)


# Finding biggest consecutive score for consonants
import re

def solve(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    conlist = re.split("a|e|i|o|u", s)
    best = 0
    for item in conlist:
        local = 0
        for con in item:
            local += abc.index(con) + 1
        best = max(best, local)
    return best

#print(solve("chruschtschov"))

# Check if squared number ends with that number
def automorphic(n):
    return 'Automorphic' if str(n * n)[-len(str(n)):] == str(n) else 'Not!!'

#print(automorphic(76))


regex = re.compile('[a-z]{4,}', re.IGNORECASE)

def replace(match):
    word = match.group(0)
    return word[0] + str(len(word) - 2) + word[-1]

def abbreviate(s):
    return regex.sub(replace, s)

def abbreviate1(input):
    return re.sub("\w+", my_replace, input)

def my_replace(m):
    w = m.group(0)
    if len(w) > 3:
        return f'{w[0]}{len(w) - 2}{w[-1]}'
    else:
        return w


#print(abbreviate('hello you-fuckers, how about dat?'))