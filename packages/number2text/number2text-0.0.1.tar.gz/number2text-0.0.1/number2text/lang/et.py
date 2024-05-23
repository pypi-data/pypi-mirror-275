_ones= ['', 'üks', 'kaks', 'kolm', 'neli', 'viis', 'kuus', 'seitse', 'kaheksa', 'üheksa']
_teens = ['kümme', 'üksteist', 'kaksteist', 'kolmteist', 'neliteist', 'viisteist', 'kuusteist', 'seitseteist', 'kaheksateist', 'üheksateist']
_tens = ['', '', 'kakskümmend', 'kolmkümmend', 'nelikümmend', 'viiskümmend', 'kuuskümmend', 'seitsekümmend', 'kaheksakümmend', 'üheksakümmend']
_hundreds = ['', 'ükssada', 'kakssada', 'kolmsada', 'nelisada', 'viissada', 'kuussada', 'seitsesada', 'kaheksasada', 'üheksasada']

_powers_of_ten = [
    ('tuhat', 'tuhat', 'tuhat'),
    ('miljon', 'miljonit', 'miljonit'),
    ('miljard', 'miljardit', 'miljardit'),
    ('triljon', 'triljonit', 'triljonit'),
    ('kvadriljon', 'kvadriljonit', 'kvadriljonit'),
    ('kvintiljon', 'kvintiljonit', 'kvintiljonit'),
    ('sekstiljon', 'sekstiljonit', 'sekstiljonit'),
    ('septiljon', 'septiljonit', 'septiljonit'),
    ('oktiljon', 'oktiljonit', 'oktiljonit'),
    ('noniljon', 'noniljonit', 'noniljonit'),
]

_fractions = {
    2: 'pool',
    3: 'kolmandik',
    4: 'neljandik',
    5: 'viiendik',
    6: 'kuuendik',
    7: 'seitsmendik',
    8: 'kaheksandik',
    9: 'üheksandik',
    10: 'kümnendik',
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
    elif number == 2:
        return _powers_of_ten[power_index][1]
    else:
        return _powers_of_ten[power_index][2]

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

        return f"{integer_words} koma {fraction_words}"

    if number == 0:
        return 'null'

    if number < 0:
        return 'miinus ' + convert(-number)

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