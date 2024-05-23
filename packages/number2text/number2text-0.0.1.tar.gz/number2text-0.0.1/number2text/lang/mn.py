_ones= ['', 'нэг', 'хоёр', 'гурав', 'дөрөв', 'тав', 'зургаа', 'долоо', 'найм', 'ес']
_teens = ['арав', 'арван нэг', 'арван хоёр', 'арван гурав', 'арван дөрөв', 'арван тав', 'арван зургаа', 'арван долоо', 'арван найм', 'арван ес']
_tens = ['', '', 'хорь', 'гуч', 'дөч', 'тавь', 'жар', 'дал', 'ная', 'ер'] 
_hundreds = ['', 'нэг зуу', 'хоёр зуу', 'гурван зуу', 'дөрвөн зуу', 'таван зуу', 'зургаан зуу', 'долоон зуу', 'найман зуу', 'есөн зуу']

_scales = [
    ('', '', ''),
    ('мянга', 'мянга', 'мянган'),
    ('сая', 'сая', 'саяын'),
    ('тэрбум', 'тэрбум', 'тэрбумын'),
    ('их наяд', 'их наяд', 'их наядын'),
    ('тунамал', 'тунамал', 'тунамалын')
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
        return 'тэг'

    if number < 0:
        return 'сөрөг ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][0 if number % 1000 == 1 else 1]
            if scale_index > 0:
                part = part + ' ' + scale  
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))