_ones= ['', 'isa', 'dalawa', 'tatlo', 'apat', 'lima', 'anim', 'pito', 'walo', 'siyam']
_teens = ['sampu', 'labing-isa', 'labindalawa', 'labintatlo', 'labing-apat', 'labinlima', 'labing-anim', 'labimpito', 'labingwalo', 'labinsiyam']
_tens = ['', '', 'dalawampu', 'tatlumpu', 'apatnapu', 'limampu', 'animnapu', 'pitumpu', 'walumpu', 'siyamnapu']
_hundreds = ['', 'isang daan', 'dalawang daan', 'tatlong daan', 'apat na raan', 'limang daan', 'anim na raan', 'pitong daan', 'walong daan', 'siyam na raan']

_scales = [
    ('', '', ''),
    ('libo', 'libo', 'libo'),
    ('milyon', 'milyong', 'milyong'),
    ('bilyon', 'bilyong', 'bilyong'),
    ('trilyon', 'trilyong', 'trilyong'),
    ('katrilyon', 'katrilyong', 'katrilyong'),
    ('kwintilyong', 'kwintilyong', 'kwintilyong'),
    ('sekstilyong', 'sekstilyong', 'sekstilyong'),
    ('septilyong', 'septilyong', 'septilyong'),
    ('oktilyong', 'oktilyong', 'oktilyong'),
    ('nonilyong', 'nonilyong', 'nonilyong'),
]

_fractions = {
    2: 'kalahati',
    3: 'ikatlo',
    4: 'ikaapat',
    5: 'ikalima',
    6: 'ikaanim',
    7: 'ikapito',
    8: 'ikawalo',
    9: 'ikasiyam',
    10: 'ikasampung'
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
            return _tens[tens] + "'t " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " at " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} at {fraction_words}"

    if number == 0:
        return 'wala'

    if number < 0:
        return 'negatibong ' + convert(-number)

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