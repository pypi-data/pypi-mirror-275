_ones= ['', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
_tens = ['', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
_scales = ['', 'bin', 'milyon', 'milyar', 'trilyon', 'katrilyon', 'kentilyon', 'seksilyon', 'septilyon', 'oktilyon', 'nonilyon', 'desilyon']

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 100:
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
            return _ones[hundreds] + ' yüz'
        else:
            return _ones[hundreds] + ' yüz ' + convert_less_than_hundred(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ''
    else:
        return ' ' + _scales[scale_index]

def convert(number):
    if number == 0:
        return 'sıfır'

    if number < 0:
        return 'eksi ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            parts.append(part + scale)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))