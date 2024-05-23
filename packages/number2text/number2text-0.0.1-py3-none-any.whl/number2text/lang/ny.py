_ones= ["", "mosi", "pili", "tatu", "nayi", "faifi", "sikisi", "seveni", "eyiti", "naini"]
_teens = ["teni", "leveni", "twelu", "tetini", "fotini", "fifitini", "sikisitini", "seventini", "eyititini", "naintini"]
_tens = ["", "", "twenti", "teti", "foti", "fifiti", "sikisiti", "seventi", "eyiti", "nainti"]
_scales = ["", "handi", "tauseni", "miliyoni", "biliyoni", "tiliyoni"]

_fractions = {
    2: 'hafu',
    3: 'thedi',
    4: 'kwota',
    5: 'fifisi',
    6: 'sikisi',
    7: 'seveni',
    8: 'eyiti',
    9: 'naini',
    10: 'teni',
}

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    else:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + "-" + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _ones[hundreds] + " handi"
        else:
            return _ones[hundreds] + " handi " + convert_less_than_hundred(less_than_hundred)

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

        return f"{integer_words} pointi {fraction_words}"

    if number == 0:
        return "ziro"

    if number < 0:
        return "mainasi " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if scale_index > 0:
                part += " " + _scales[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))