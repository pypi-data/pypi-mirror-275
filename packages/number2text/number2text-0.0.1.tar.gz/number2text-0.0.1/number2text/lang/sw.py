_ones= ['', 'moja', 'mbili', 'tatu', 'nne', 'tano', 'sita', 'saba', 'nane', 'tisa']
_teens = ['kumi', 'kumi na moja', 'kumi na mbili', 'kumi na tatu', 'kumi na nne', 'kumi na tano', 'kumi na sita', 'kumi na saba', 'kumi na nane', 'kumi na tisa']
_tens = ['', '', 'ishirini', 'thelathini', 'arobaini', 'hamsini', 'sitini', 'sabini', 'themanini', 'tisini']
_scales = ['', 'elfu', 'milioni', 'bilioni', 'trilioni', 'kuadrilioni', 'kuintilioni', 'sekstilioni', 'septilioni', 'oktilioni', 'nonilioni', 'desilioni']

_fractions = {
    2: 'nusu',
    3: 'theluthi',
    4: 'robo',
    5: 'tano',
    6: 'sita',
    7: 'saba',
    8: 'nane',
    9: 'tisa',
    10: 'kumi',
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
            return _tens[tens] + ' na ' + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _ones[hundreds] + ' mia'
        else:
            return _ones[hundreds] + ' mia ' + convert_less_than_hundred(less_than_hundred)

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + ' ya ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} nukta {fraction_words}"

    if number == 0:
        return 'sifuri'

    if number < 0:
        return 'hasi ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if scale_index > 0:
                part += ' ' + _scales[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))