_ones= ['', 'usa', 'duha', 'tulo', 'upat', 'lima', 'unom', 'pito', 'walo', 'siyam']
_teens = ['napulo', 'napulog usa', 'napulog duha', 'napulog tulo', 'napulog upat', 'napulog lima', 'napulog unom', 'napulog pito', 'napulog walo', 'napulog siyam']
_tens = ['', '', 'kawhaan', 'katloan', 'kap-atan', 'kalim-an', 'kan-uman', 'kapitoan', 'kawaloan', 'kasiyaman']
_hundreds = ['', 'usa ka gatos', 'duha ka gatos', 'tulo ka gatos', 'upat ka gatos', 'lima ka gatos', 'unom ka gatos', 'pito ka gatos', 'walo ka gatos', 'siyam ka gatos']

_scales = [
    ('', '', ''),
    ('libo', 'ka libo', 'ka libo'),
    ('milyon', 'ka milyon', 'ka milyon'),
    ('bilyon', 'ka bilyon', 'ka bilyon'),
    ('trilyon', 'ka trilyon', 'ka trilyon'),
    ('kwadrilyon', 'ka kwadrilyon', 'ka kwadrilyon'),
    ('kwintilyon', 'ka kwintilyon', 'ka kwintilyon'),
    ('sekstilyon', 'ka sekstilyon', 'ka sekstilyon'),
    ('septilyon', 'ka septilyon', 'ka septilyon'),
    ('oktilyon', 'ka oktilyon', 'ka oktilyon'),
    ('nonilyon', 'ka nonilyon', 'ka nonilyon'),
    ('desilyon', 'ka desilyon', 'ka desilyon')
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
            return _tens[tens] + ' ' + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_hundred(less_than_hundred)
        
def convert(number):
    if number == 0:
        return 'zero'

    if number < 0:
        return 'negatibo ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][1 if number % 1000 == 1 else 2]
            if scale_index > 0:
                part = part + ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))