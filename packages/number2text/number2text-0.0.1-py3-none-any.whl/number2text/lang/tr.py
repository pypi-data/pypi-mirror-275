_ones= ['', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
_teens = ['on', 'on bir', 'on iki', 'on üç', 'on dört', 'on beş', 'on altı', 'on yedi', 'on sekiz', 'on dokuz']
_tens = ['', '', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
_scales = ['', 'bin', 'milyon', 'milyar', 'trilyon', 'katrilyon', 'kentilyon', 'sekstilyon', 'septilyon', 'oktilyon', 'nonilyon', 'desilyon']

_fractions = {
    2: 'yarım',
    3: 'üçte bir',
    4: 'çeyrek', 
    5: 'beşte bir',
    6: 'altıda bir',
    7: 'yedide bir',
    8: 'sekizde bir',
    9: 'dokuzda bir',
    10: 'onda bir',
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

        return f"{integer_words} virgül {fraction_words}"

    if number == 0:
        return 'sıfır'

    if number < 0:
        return 'eksi ' + convert(-number)

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