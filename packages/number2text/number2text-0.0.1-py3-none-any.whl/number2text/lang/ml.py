_ones= ['', 'eka', 'dvi', 'tri', 'chatur', 'pancha', 'shhat', 'sapta', 'ashta', 'nava']
_teens = ['dasha', 'ekadasha', 'dvadasha', 'trayodasha', 'chaturdasha', 'panchadasha', 'shodasha', 'saptadasha', 'ashtadasha', 'ekonavimshat']  
_tens = ['', '', 'vimshat', 'trimshat', 'chatvaarimshat', 'panchaashat', 'shashti', 'saptati', 'asiti', 'navati']
_hundreds = ['', 'shata', 'dvi-shata', 'tri-shata', 'chatur-shata', 'pancha-shata', 'shhat-shata', 'sapta-shata', 'ashta-shata', 'nava-shata']

_scales = [
    ('', '', ''),
    ('sahasra', 'sahasre', 'sahasraani'),
    ('laksha', 'lakshe', 'lakshaani'), 
    ('koti', 'kotye', 'kotyah'),
    ('arbuda', 'arbude', 'arbudaani'),
    ('abja', 'abje', 'abjaani'),
    ('kharva', 'kharve', 'kharvaani'),
    ('nikharva', 'nikharve', 'nikharvaani'),
    ('mahapadma', 'mahapadme', 'mahapadmaani'),
    ('shankha', 'shankhe', 'shankhaani'),
]

_fractions = {
    2: 'ardha',
    3: 'trtiiya',
    4: 'chaturtha',  
    5: 'panchama',
    6: 'shashtha',
    7: 'saptama',
    8: 'ashtama',
    9: 'navama',
    10: 'dashama'
}

def get_ones(digit):
    return _ones[digit]

def get_teens(number):
    return _teens[number-10]

def get_tens(number):
    return _tens[number]

def get_hundreds(number):
    return _hundreds[number]

def get_scale(number, scale_index):
    if number == 1:
        return _scales[scale_index][0]
    elif number == 2:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_less_than_thousand(number):
    if number < 10:
        return get_ones(number)
    elif number < 20:
        return get_teens(number)
    elif number < 100:
        tens, ones = divmod(number, 10)
        result = get_tens(tens)
        if ones > 0:
            result += ' ' + get_ones(ones)
        return result
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        result = get_hundreds(hundreds)
        if less_than_hundred > 0:
            result += ' ' + convert_less_than_thousand(less_than_hundred)
        return result

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

        return f"{integer_words} dasha-amsha {fraction_words}"

    if number == 0:
        return 'shunya'

    if number < 0:
        return 'rna ' + convert(-number)

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