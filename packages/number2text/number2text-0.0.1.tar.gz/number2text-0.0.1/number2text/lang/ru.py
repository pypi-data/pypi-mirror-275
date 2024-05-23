_ones = {
    1: ('один', 'одна', 'одно'),
    2: ('два', 'две', 'два'),
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять'
}
_teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать',
          'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
_tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят',
         'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
_hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот',
             'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']

_scales = [
    ('тысяча', 'тысячи', 'тысяч'),         # 10^3
    ('миллион', 'миллиона', 'миллионов'),  # 10^6
    ('миллиард', 'миллиарда', 'миллиардов'), # 10^9
    ('триллион', 'триллиона', 'триллионов'), # 10^12
    ('квадриллион', 'квадриллиона', 'квадриллионов'), # 10^15
    ('квинтиллион', 'квинтиллиона', 'квинтиллионов'), # 10^18
    ('секстиллион', 'секстиллиона', 'секстиллионов'), # 10^21
    ('септиллион', 'септиллиона', 'септиллионов'), # 10^24
    ('октиллион', 'октиллиона', 'октиллионов'), # 10^27
    ('нониллион', 'нониллиона', 'нониллионов'), # 10^30
]

_fractions = {
    2: 'половина',
    3: 'треть',
    4: 'четверть',
    5: 'пятая',
    6: 'шестая',
    7: 'седьмая',
    8: 'восьмая',
    9: 'девятая',
    10: 'десятая',
    # ...
}

def get_ones(digit, gender):
    if digit == 1:
        return _ones[digit][gender]
    elif digit == 2:
        if gender == 1:  # Feminine
            return 'две'
        elif gender == 2:  # Neuter
            return 'два'
        else:  # Masculine
            return 'два'
    else:
        return _ones[digit]


def get_scale(number, scale_index):
    if 10 < number % 100 < 20:
        return _scales[scale_index][2]
    elif number % 10 == 1:
        return _scales[scale_index][0]
    elif 1 < number % 10 < 5:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_less_than_thousand(number, gender):
    if number < 10:
        return get_ones(number, gender)
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        return _tens[tens] + ((" " + get_ones(ones, gender)) if ones else "")
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred, gender)

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator] + ("" if numerator in [2,3,4] else "ых")

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} целых {fraction_words}"

    if number == 0:
        return 'ноль'

    if number < 0:
        return 'минус ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            if scale_index == 0:
                gender = 2 if number % 10 == 1 and number % 100 != 11 else 1
            else:
                gender = 1
            part = convert_less_than_thousand(number % 1000, gender)
            if scale_index > 0:
                part += " " + get_scale(number % 1000, scale_index - 1)
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))
