_ones= ['', 'unu', 'doi', 'trei', 'patru', 'cinci', 'șase', 'șapte', 'opt', 'nouă']
_teens = ['zece', 'unsprezece', 'doisprezece', 'treisprezece', 'paisprezece', 'cincisprezece', 'șaisprezece', 'șaptesprezece', 'optsprezece', 'nouăsprezece']
_tens = ['', '', 'douăzeci', 'treizeci', 'patruzeci', 'cincizeci', 'șaizeci', 'șaptezeci', 'optzeci', 'nouăzeci']
_hundreds = ['', 'o sută', 'două sute', 'trei sute', 'patru sute', 'cinci sute', 'șase sute', 'șapte sute', 'opt sute', 'nouă sute']

_scales = [
    ('', '', ''),
    ('o mie', 'mii', 'de mii'),
    ('un milion', 'milioane', 'de milioane'),
    ('un miliard', 'miliarde', 'de miliarde'),
    ('un trilion', 'trilioane', 'de trilioane'),
    ('un cvadriliard', 'cvadriliarde', 'de cvadriliarde'),
    ('un cvintilion', 'cvintilioane', 'de cvintilioane'),
    ('un sextilion', 'sextilioane', 'de sextilioane'),
    ('un septilion', 'septilioane', 'de septilioane'),
    ('un octilion', 'octilioane', 'de octilioane'),
    ('un nonilion', 'nonilioane', 'de nonilioane'),
    ('un decilion', 'decilioane', 'de decilioane'),
]

_fractions = {
    2: 'doime',
    3: 'treime',
    4: 'pătrime',
    5: 'cincime',
    6: 'șesime',
    7: 'șeptime',
    8: 'optime',
    9: 'nouime',
    10: 'zecime',
}

def convert_less_than_thousand(number, feminine=False):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + ' și ' + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            if feminine and hundreds == 1:
                return 'o sută'
            else:
                return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_thousand(less_than_hundred, feminine)

def get_scale(number, scale_index, feminine=False):
    if scale_index == 0:
        return ''
    elif number == 1:
        return _scales[scale_index][0]
    elif number < 20:
        return _scales[scale_index][1]
    else:
        if feminine:
            return _scales[scale_index][1]
        else:
            return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + ' ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} virgulă {fraction_words}"

    if number == 0:
        return 'zero'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    scale_index = 0
    feminine = False
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000, feminine)
            scale = get_scale(number % 1000, scale_index, feminine)
            if scale:
                part += ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1
        feminine = True

    return ' '.join(reversed(parts))