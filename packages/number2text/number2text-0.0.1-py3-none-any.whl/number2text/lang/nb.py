_ones= ['', 'en', 'to', 'tre', 'fire', 'fem', 'seks', 'sju', 'åtte', 'ni']
_teens = ['ti', 'elleve', 'tolv', 'tretten', 'fjorten', 'femten', 'seksten', 'sytten', 'atten', 'nitten']
_tens = ['', '', 'tjue', 'tretti', 'førti', 'femti', 'seksti', 'sytti', 'åtti', 'nitti']
_hundreds = ['', 'ett hundre', 'to hundre', 'tre hundre', 'fire hundre', 'fem hundre', 'seks hundre', 'sju hundre', 'åtte hundre', 'ni hundre']

_scales = [
    ('', '', ''),
    ('tusen', 'tusen', 'tusen'),
    ('million', 'millioner', 'millioner'),
    ('milliard', 'milliarder', 'milliarder'),
    ('billion', 'billioner', 'billioner'),
    ('billiard', 'billiarder', 'billiarder'),
]

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
            return _tens[tens] + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        elif hundreds == 1:
            return 'ett hundre og ' + convert_less_than_hundred(less_than_hundred)
        else:
            return _hundreds[hundreds] + ' og ' + convert_less_than_hundred(less_than_hundred)

def convert(number):
    if number == 0:
        return 'null'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][0 if number % 1000 == 1 else 1]
            if scale_index > 0:
                part += ' ' + scale  
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))