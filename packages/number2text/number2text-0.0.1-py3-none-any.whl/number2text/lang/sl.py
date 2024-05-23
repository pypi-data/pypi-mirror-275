_ones= ['', 'ena', 'dva', 'tri', 'štiri', 'pet', 'šest', 'sedem', 'osem', 'devet']
_teens = ['deset', 'enajst', 'dvanajst', 'trinajst', 'štirinajst', 'petnajst', 'šestnajst', 'sedemnajst', 'osemnajst', 'devetnajst']
_tens = ['', '', 'dvajset', 'trideset', 'štirideset', 'petdeset', 'šestdeset', 'sedemdeset', 'osemdeset', 'devetdeset']
_hundreds = ['', 'sto', 'dvesto', 'tristo', 'štiristo', 'petsto', 'šeststo', 'sedemsto', 'osemsto', 'devetsto']

_scales = [
    ('', '', ''),
    ('tisoč', 'tisoč', 'tisoč'),
    ('milijon', 'milijona', 'milijonov'),
    ('milijarda', 'milijardi', 'milijard'),
    ('bilijon', 'bilijona', 'bilijonov'),
    ('bilijarda', 'bilijardi', 'bilijard'),
    ('trilijon', 'trilijona', 'trilijonov'),
    ('trilijarda', 'trilijardi', 'trilijard'),
    ('kvadrilijon', 'kvadrilijona', 'kvadrilijonov'),
    ('kvadrilijarda', 'kvadrilijardi', 'kvadrilijard'),
    ('kvintilijon', 'kvintilijonov', 'kvintilijonov'),
    ('kvintilijonov', 'kvintilijonov', 'kvintilijonov'),
]

_fractions = {
    2: 'polovica',
    3: 'tretjina',
    4: 'četrtina',
    5: 'petina',
    6: 'šestina',
    7: 'sedmina',
    8: 'osmina',
    9: 'devetina',
    10: 'desetina',
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
            return _tens[tens] + ' ' + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ''
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
        return convert(numerator) + ' ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} in {fraction_words}"

    if number == 0:
        return 'nič'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))