_ones= {
    1: ('واحد', 'واحدة'),
    2: ('اثنان', 'اثنتان'),
    3: 'ثلاثة',
    4: 'أربعة',
    5: 'خمسة',
    6: 'ستة',
    7: 'سبعة',
    8: 'ثمانية',
    9: 'تسعة'
}
_teens = ['عشرة', 'أحد عشر', 'اثنا عشر', 'ثلاثة عشر', 'أربعة عشر',
          'خمسة عشر', 'ستة عشر', 'سبعة عشر', 'ثمانية عشر', 'تسعة عشر']
_tens = ['', '', 'عشرون', 'ثلاثون', 'أربعون', 'خمسون',
         'ستون', 'سبعون', 'ثمانون', 'تسعون']
_hundreds = ['', 'مائة', 'مائتان', 'ثلاثمائة', 'أربعمائة', 'خمسمائة',
             'ستمائة', 'سبعمائة', 'ثمانمائة', 'تسعمائة']

_scales = [
    ('ألف', 'ألفان', 'آلاف'),         
    ('مليون', 'مليونان', 'ملايين'),  
    ('مليار', 'ملياران', 'مليارات'), 
    ('ترليون', 'ترليونان', 'ترليونات'), 
    ('كوادرليون', 'كوادرليونان', 'كوادرليونات'), 
    ('كوينتليون', 'كوينتليونان', 'كوينتليونات'), 
    ('سكستليون', 'سكستليونان', 'سكستليونات'), 
    ('سبتليون', 'سبتليونان', 'سبتليونات'), 
    ('أوكتليون', 'أوكتليونان', 'أوكتليونات'), 
    ('نونيليون', 'نونيليونان', 'نونيليونات'), 
]

_fractions = {
    2: 'نصف',
    3: 'ثلث',
    4: 'ربع',
    5: 'خمس',
    6: 'سدس',
    7: 'سبع',
    8: 'ثمن',
    9: 'تسع',
    10: 'عشر',
}

def get_ones(digit, gender):
    if digit == 1:
        return _ones[digit][gender]
    elif digit == 2:
        return _ones[digit][gender]
    else:
        return _ones[digit]


def get_scale(number, scale_index):
    if 3 <= number <= 10:
        return _scales[scale_index][2]
    elif number == 2:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][0]

def convert_less_than_thousand(number, gender):
    if number < 10:
        return get_ones(number, gender)
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        return _tens[tens] + ((" و" + get_ones(ones, gender)) if ones else "")
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " و" + convert_less_than_thousand(less_than_hundred, gender)

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} فاصلة {fraction_words}"

    if number == 0:
        return 'صفر'

    if number < 0:
        return 'سالب ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            if scale_index == 0:
                gender = 0 if number % 10 in [1, 2] else 1
            else:
                gender = 1
            part = convert_less_than_thousand(number % 1000, gender)
            if scale_index > 0:
                part += " " + get_scale(number % 1000, scale_index - 1)
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " و".join(reversed(parts))