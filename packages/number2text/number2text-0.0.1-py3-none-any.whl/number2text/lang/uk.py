_ones= ["", "один", "два", "три", "чотири", "п'ять", "шість", "сім", "вісім", "дев'ять"]
_teens = ["десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п'ятнадцять", "шістнадцять", "сімнадцять", "вісімнадцять", "дев'ятнадцять"]
_tens = ["", "", "двадцять", "тридцять", "сорок", "п'ятдесят", "шістдесят", "сімдесят", "вісімдесят", "дев'яносто"]
_hundreds = ["", "сто", "двісті", "триста", "чотириста", "п'ятсот", "шістсот", "сімсот", "вісімсот", "дев'ятсот"]

_scales = [
    ("", "", ""),
    ("тисяча", "тисячі", "тисяч"),
    ("мільйон", "мільйони", "мільйонів"),
    ("мільярд", "мільярди", "мільярдів"),
    ("трильйон", "трильйони", "трильйонів"),
    ("квадрильйон", "квадрильйони", "квадрильйонів"),
    ("квінтильйон", "квінтильйони", "квінтильйонів"),
    ("секстильйон", "секстильйони", "секстильйонів"),
    ("септильйон", "септильйони", "септильйонів"),
    ("октильйон", "октильйони", "октильйонів"),
    ("нонильйон", "нонильйони", "нонильйонів"),
    ("децильйон", "децильйони", "децильйонів"),
]

_fractions = {
    2: 'половина',
    3: 'третина',
    4: 'чверть',
    5: 'п\'ята',
    6: 'шоста',
    7: 'сьома',
    8: 'восьма',
    9: 'дев\'ята',
    10: 'десята',
}

def convert_less_than_thousand(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + " " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif 1 < number < 5:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator] + ("и" if numerator > 1 else "а")

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} кома {fraction_words}"

    if number == 0:
        return "нуль"

    if number < 0:
        return "мінус " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))