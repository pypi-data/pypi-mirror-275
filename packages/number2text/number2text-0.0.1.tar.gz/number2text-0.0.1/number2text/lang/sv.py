_ones= ['', 'ett', 'två', 'tre', 'fyra', 'fem', 'sex', 'sju', 'åtta', 'nio']
_teens = ['tio', 'elva', 'tolv', 'tretton', 'fjorton', 'femton', 'sexton', 'sjutton', 'arton', 'nitton']
_tens = ['', '', 'tjugo', 'trettio', 'fyrtio', 'femtio', 'sextio', 'sjuttio', 'åttio', 'nittio']
_hundreds = ['', 'etthundra', 'tvåhundra', 'trehundra', 'fyrahundra', 'femhundra', 'sexhundra', 'sjuhundra', 'åttahundra', 'niohundra']

_scales = [
    ('', '', ''),
    ('tusen', 'tusen', 'tusen'),
    ('miljon', 'miljoner', 'miljoner'),
    ('miljard', 'miljarder', 'miljarder'),
    ('biljon', 'biljoner', 'biljoner'),
    ('biljard', 'biljarder', 'biljarder'),
    ('triljon', 'triljoner', 'triljoner'),
    ('triljard', 'triljarder', 'triljarder'),
    ('kvadriljon', 'kvadriljoner', 'kvadriljoner'),
    ('kvadriljard', 'kvadriljarder', 'kvadriljarder'),
    ('kvintiljon', 'kvintiljoner', 'kvintiljoner'),
    ('kvintiljard', 'kvintiljarder', 'kvintiljarder')
]

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number-10]
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
            return 'hundra' + convert_less_than_hundred(less_than_hundred)
        else:
            return _hundreds[hundreds] + convert_less_than_hundred(less_than_hundred)
            
def convert(number):
    if number == 0:
        return 'noll'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][1 if number % 1000 == 1 else 2]
            if scale_index > 0:
                part += ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))