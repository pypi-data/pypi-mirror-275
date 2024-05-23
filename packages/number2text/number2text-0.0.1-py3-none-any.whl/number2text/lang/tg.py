_ones= ['', 'unu', 'du', 'tri', 'kvar', 'kvin', 'ses', 'sep', 'ok', 'naŭ']
_teens = ['dek', 'dek unu', 'dek du', 'dek tri', 'dek kvar', 'dek kvin', 'dek ses', 'dek sep', 'dek ok', 'dek naŭ'] 
_tens = ['', '', 'dudek', 'tridek', 'kvardek', 'kvindek', 'sesdek', 'sepdek', 'okdek', 'naŭdek']
_hundreds = ['', 'cent', 'ducent', 'tricent', 'kvarcent', 'kvincent', 'sescent', 'sepcent', 'okcent', 'naŭcent']

_powers_of_ten = [
    ('mil', 'mil'), 
    ('miliono', 'milionoj'),
    ('miliardo', 'miliardoj'),
    ('biliono', 'bilionoj'),
    ('biliardo', 'biliardoj'),
    ('triliono', 'trilionoj')
]

_fractions = {
    2: 'duono',
    3: 'triono', 
    4: 'kvarono',
    5: 'kvinono',
    6: 'sesono',
    7: 'sepono',
    8: 'okono',
    9: 'naŭono',
    10: 'dekono'
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

def get_power(number, power_index):
    if number == 1:
        return _powers_of_ten[power_index][0]
    else:
        return _powers_of_ten[power_index][1]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + ' ' + _fractions[denominator] + 'j'

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} komo {fraction_words}"

    if number == 0:
        return 'nul'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    power_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            power = get_power(number % 1000, power_index)  
            if power:
                part += ' ' + power
            parts.append(part)
        number //= 1000
        power_index += 1

    return ' '.join(reversed(parts))