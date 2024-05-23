_ones= ['', 'ikk', 'do', 'tinn', 'chaar', 'panj', 'chhe', 'satt', 'atth', 'nauv']
_teens = ['das', 'gyaaraa', 'baaraa', 'teraa', 'chaudaa', 'pandraa', 'solaa', 'satraa', 'atthaaraa', 'unnee']
_tens = ['', '', 'vee', 'tee', 'chaalee', 'panjaa', 'satth', 'sattar', 'assee', 'nabbe'] 
_hundreds = ['', 'ikk sau', 'do sau', 'tinn sau', 'chaar sau', 'panj sau', 'chhe sau', 'satt sau', 'atth sau', 'nauv sau']

_scales = [
    ('', '', ''),
    ('hazaar', 'hazaar', 'hazaar'),
    ('lakh', 'lakh', 'lakh'),
    ('karor', 'karor', 'karor'),
    ('arab', 'arab', 'arab'),
    ('kharab', 'kharab', 'kharab'),
    ('neel', 'neel', 'neel'),
    ('padma', 'padma', 'padma'),
    ('shankh', 'shankh', 'shankh')
]

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number-10]
    else:
        tens, ones = divmod(number, 10)
        if ones > 0:
            return _tens[tens] + ' ' + _ones[ones]
        else:
            return _tens[tens]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, tens = divmod(number, 100)
        if tens > 0:
            return _hundreds[hundreds] + ' ' + convert_less_than_hundred(tens)
        else:
            return _hundreds[hundreds]

def convert(number):
    if number == 0:
        return 'sifar'
    
    if number < 0:
        return 'ghaatt ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][0]
            if scale_index > 0:
                part = part + ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))