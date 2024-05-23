_ones= ['', 'un', 'dau', 'tri', 'pedwar', 'pump', 'chwech', 'saith', 'wyth', 'naw']
_teens = ['deg', 'un ar ddeg', 'deuddeg', 'tri ar ddeg', 'pedwar ar ddeg', 'pymtheg', 'un ar bymtheg', 'dau ar bymtheg', 'deunaw', 'pedwar ar bymtheg'] 
_tens = ['', '', 'ugain', 'deg ar hugain', 'deugain', 'hanner cant', 'trigain', 'deg a thrigain', 'pedwar ugain', 'deg a phedwar ugain']
_hundreds = ['', 'cant', 'dau gant', 'tri chant', 'pedwar cant', 'pum cant', 'chwe chant', 'saith gant', 'wyth gant', 'naw cant']

_scales = [
    ('', '', ''),
    ('mil', 'mil', 'mil'),
    ('miliwn', 'miliynau', 'miliynau'), 
    ('biliwn', 'biliynau', 'biliynau'),
    ('triliwn', 'triliynau', 'triliynau'),
    ('cwadriliwn', 'cwadriliwn', 'cwadriliwn'),
    ('cwintiliwn', 'cwintiliwn', 'cwintiliwn'),
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
        elif tens == 1:
            return _ones[ones] + ' ar ddeg'
        else:
            return _tens[tens] + ' ' + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        elif hundreds == 1:
            return 'cant a ' + convert_less_than_hundred(less_than_hundred)
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_hundred(less_than_hundred)

def convert(number):
    if number == 0:
        return 'sero'

    if number < 0:
        return 'minws ' + convert(-number)

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