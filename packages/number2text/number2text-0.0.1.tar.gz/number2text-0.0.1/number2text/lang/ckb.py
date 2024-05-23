_ones= ['', 'یەک', 'دوو', 'سێ', 'چوار', 'پێنج', 'شەش', 'حەوت', 'هەشت', 'نۆ']
_teens = ['دە', 'یازدە', 'دوازدە', 'سێزدە', 'چواردە', 'پازدە', 'شازدە', 'حەڤدە', 'هەژدە', 'نۆزدە'] 
_tens = ['', '', 'بیست', 'سی', 'چل', 'پەنجا', 'شەست', 'حەفتا', 'هەشتا', 'نەوەد']
_hundreds = ['', 'سەد', 'دووسەد', 'سێسەد', 'چوارسەد', 'پێنجسەد', 'شەشسەد', 'حەوتسەد', 'هەشتسەد', 'نۆسەد']

_scales = [
    ('', '', ''),
    ('هەزار', 'هەزار', 'هەزار'),
    ('میلیۆن', 'میلیۆن', 'میلیۆن'),
    ('میلیارد', 'میلیارد', 'میلیارد'),
    ('تریلیۆن', 'تریلیۆن', 'تریلیۆن'),
    ('تریلیارد', 'تریلیارد', 'تریلیارد'),
    ('کوادریلیۆن', 'کوادریلیۆن', 'کوادریلیۆن'),
    ('کوادریلیارد', 'کوادریلیارد', 'کوادریلیارد'),
    ('کوینتیلیۆن', 'کوینتیلیۆن', 'کوینتیلیۆن'),
    ('کوینتیلیارد', 'کوینتیلیارد', 'کوینتیلیارد'),
    ('سێکستیلیۆن', 'سێکستیلیۆن', 'سێکستیلیۆن'),
    ('سێکستیلیارد', 'سێکستیلیارد', 'سێکستیلیارد'),
]

_fractions = {
    2: 'نیو',
    3: 'سێیەک',
    4: 'چارەک',
    5: 'پێنجەک',
    6: 'شەشەک',
    7: 'حەوتەک',
    8: 'هەشتەک',
    9: 'نۆیەک',
    10: 'دەیەک',
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
            return _tens[tens] + ' و ' + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' و ' + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ''
    elif number == 1:
        return _scales[scale_index][0]
    elif 1 < number < 10:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + 'ی ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} ڕاستە {fraction_words}"

    if number == 0:
        return 'سفر'

    if number < 0:
        return 'نێگەتیڤ ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' و '.join(reversed(parts))