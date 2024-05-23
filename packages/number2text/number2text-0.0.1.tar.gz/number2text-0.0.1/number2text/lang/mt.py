_ones= ['', 'ⴰⵢⴰⵏ', 'ⵙⵉⵏ', 'ⴽⵔⴰⴹ', 'ⴽⴽⵓⵥ', 'ⵙⵉⵎⵎⵓⵙ', 'ⵙⴹⵉⵙ', 'ⵙⴰ', 'ⵜⵜⴰⵎ', 'ⵜⵜⵣⴰ']
_teens = ['ⵎⵔⴰⵡ', 'ⵎⵔⴰⵡ ⴷ ⵉⵊⵊ', 'ⵎⵔⴰⵡ ⴷ ⵙⵉⵏ', 'ⵎⵔⴰⵡ ⴷ ⴽⵔⴰⴹ', 'ⵎⵔⴰⵡ ⴷ ⴽⴽⵓⵥ', 'ⵎⵔⴰⵡ ⴷ ⵙⵉⵎⵎⵓⵙ', 'ⵎⵔⴰⵡ ⴷ ⵙⴹⵉⵙ', 'ⵎⵔⴰⵡ ⴷ ⵙⴰ', 'ⵎⵔⴰⵡ ⴷ ⵜⵜⴰⵎ', 'ⵎⵔⴰⵡ ⴷ ⵜⵜⵣⴰ']
_tens = ['', '', 'ⵙⵉⵏⴰⵜ', 'ⵜⵍⴰⵜⵉⵏ', 'ⵔⴱⵄⵉⵏ', 'ⵚⵎⵙⵉⵏ', 'ⵙⵜⵜⵉⵏ', 'ⵙⴰⵜⵜⵉⵏ', 'ⵜⵜⵎⴰⵏⵉⵏ', 'ⵜⵜⵣⵉⵏ']
_hundreds = ['', 'ⵎⵉⵢⴰ', 'ⵙⵉⵏ ⵎⵉⵢⴰ', 'ⴽⵔⴰⴹ ⵎⵉⵢⴰ', 'ⴽⴽⵓⵥ ⵎⵉⵢⴰ', 'ⵙⵉⵎⵎⵓⵙ ⵎⵉⵢⴰ', 'ⵙⴹⵉⵙ ⵎⵉⵢⴰ', 'ⵙⴰ ⵎⵉⵢⴰ', 'ⵜⵜⴰⵎ ⵎⵉⵢⴰ', 'ⵜⵜⵣⴰ ⵎⵉⵢⴰ']

_scales = [
    ('', '', ''),
    ('ⴰⴳⵉⵎ', 'ⴰⴳⵉⵎ', 'ⴰⴳⵉⵎ'),
    ('ⴰⵎⵉⵍⵢⵓⵏ', 'ⵉⵎⵉⵍⵢⵓⵏⵏ', 'ⵉⵎⵉⵍⵢⵓⵏⵏ'),
    ('ⴰⵎⵉⵍⵢⴰⵔ', 'ⵉⵎⵉⵍⵢⴰⵔⵏ', 'ⵉⵎⵉⵍⵢⴰⵔⵏ'),
    ('ⴰⵜⵔⵉⵍⵢⵓⵏ', 'ⵉⵜⵔⵉⵍⵢⵓⵏⵏ', 'ⵉⵜⵔⵉⵍⵢⵓⵏⵏ'),
    ('ⴰⵜⵔⵉⵍⵢⴰⵔ', 'ⵉⵜⵔⵉⵍⵢⴰⵔⵏ', 'ⵉⵜⵔⵉⵍⵢⴰⵔⵏ'),
    ('ⴰⴽⵡⴰⴷⵔⵉⵍⵢⵓⵏ', 'ⵉⴽⵡⴰⴷⵔⵉⵍⵢⵓⵏⵏ', 'ⵉⴽⵡⴰⴷⵔⵉⵍⵢⵓⵏⵏ'),
    ('ⴰⴽⵡⴰⴷⵔⵉⵍⵢⴰⵔ', 'ⵉⴽⵡⴰⴷⵔⵉⵍⵢⴰⵔⵏ', 'ⵉⴽⵡⴰⴷⵔⵉⵍⵢⴰⵔⵏ'),
    ('ⴰⴽⵡⵉⵏⵜⵉⵍⵢⵓⵏ', 'ⵉⴽⵡⵉⵏⵜⵉⵍⵢⵓⵏⵏ', 'ⵉⴽⵡⵉⵏⵜⵉⵍⵢⵓⵏⵏ'),
    ('ⴰⴽⵡⵉⵏⵜⵉⵍⵢⴰⵔ', 'ⵉⴽⵡⵉⵏⵜⵉⵍⵢⴰⵔⵏ', 'ⵉⴽⵡⵉⵏⵜⵉⵍⵢⴰⵔⵏ'),
    ('ⴰⵙⵉⴽⵙⵜⵉⵍⵢⵓⵏ', 'ⵉⵙⵉⴽⵙⵜⵉⵍⵢⵓⵏⵏ', 'ⵉⵙⵉⴽⵙⵜⵉⵍⵢⵓⵏⵏ'),
    ('ⴰⵙⵉⴽⵙⵜⵉⵍⵢⴰⵔ', 'ⵉⵙⵉⴽⵙⵜⵉⵍⵢⴰⵔⵏ', 'ⵉⵙⵉⴽⵙⵜⵉⵍⵢⴰⵔⵏ'),
]

_fractions = {
    2: 'ⴰⵣⴳⵏ', 
    3: 'ⴰⴽⵔⴰⴹ',
    4: 'ⴰⴽⴽⵓⵥ',
    5: 'ⴰⵙⵉⵎⵎⵓⵙ',
    6: 'ⴰⵙⴹⵉⵙ',
    7: 'ⴰⵙⴰ',
    8: 'ⴰⵜⵜⴰⵎ',
    9: 'ⴰⵜⵜⵣⴰ',
    10: 'ⴰⵎⵔⴰⵡ',
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
            return _tens[tens] + ' ⴷ ' + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' ⴷ ' + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ''
    elif number == 1:
        return _scales[scale_index][0]
    elif 1 < number < 10:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + ' ⵏ ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} ⴷ {fraction_words}"

    if number == 0:
        return 'ⴰⵎⵢⴰ'

    if number < 0:
        return 'ⵎⵉⵏⵓⵙ ' + convert(-number)

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

    return ' ⴷ '.join(reversed(parts))