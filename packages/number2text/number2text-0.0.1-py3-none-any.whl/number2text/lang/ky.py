_ones= ["", "бир", "эки", "үч", "төрт", "беш", "алты", "жети", "сегиз", "тогуз"]
_teens = ["он", "он бир", "он эки", "он үч", "он төрт", "он беш", "он алты", "он жети", "он сегиз", "он тогуз"]
_tens = ["", "", "жыйырма", "отуз", "кырк", "элүү", "алтымыш", "жетимиш", "сексен", "токсон"]
_hundreds = ["", "жүз", "эки жүз", "үч жүз", "төрт жүз", "беш жүз", "алты жүз", "жети жүз", "сегиз жүз", "тогуз жүз"]

_scales = [
    ("", "", ""),
    ("миң", "миң", "миң"),
    ("миллион", "миллион", "миллион"),
    ("миллиард", "миллиард", "миллиард"),
    ("триллион", "триллион", "триллион"),
    ("триллиард", "триллиард", "триллиард"),
    ("квадриллион", "квадриллион", "квадриллион"),
    ("квадриллиард", "квадриллиард", "квадриллиард"),
    ("квинтиллион", "квинтиллион", "квинтиллион"),
    ("квинтиллиард", "квинтиллиард", "квинтиллиард"),
    ("секстиллион", "секстиллион", "секстиллион"),
    ("секстиллиард", "секстиллиард", "секстиллиард"),
]

_fractions = {
    2: 'жарым',
    3: 'үчтөн бир',
    4: 'төрттөн бир',
    5: 'бештен бир',
    6: 'алтыдан бир',
    7: 'жетиден бир',
    8: 'сегизден бир',
    9: 'тогуздан бир',
    10: 'ондон бир',
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
    else:
        return _scales[scale_index][1]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} бүтүн {fraction_words}"

    if number == 0:
        return "нөл"

    if number < 0:
        return "минус " + convert(-number)

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