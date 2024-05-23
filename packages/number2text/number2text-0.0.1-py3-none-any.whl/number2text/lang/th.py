_ones= ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
_teens = ['สิบ', 'สิบเอ็ด', 'สิบสอง', 'สิบสาม', 'สิบสี่', 'สิบห้า', 'สิบหก', 'สิบเจ็ด', 'สิบแปด', 'สิบเก้า']
_tens = ['', '', 'ยี่สิบ', 'สามสิบ', 'สี่สิบ', 'ห้าสิบ', 'หกสิบ', 'เจ็ดสิบ', 'แปดสิบ', 'เก้าสิบ']
_hundreds = ['', 'หนึ่งร้อย', 'สองร้อย', 'สามร้อย', 'สี่ร้อย', 'ห้าร้อย', 'หกร้อย', 'เจ็ดร้อย', 'แปดร้อย', 'เก้าร้อย']

_scales = [
    ('พัน', 'หมื่น', 'แสน'),
    ('ล้าน', 'สิบล้าน', 'ร้อยล้าน'),
    ('พันล้าน', 'หมื่นล้าน', 'แสนล้าน'),
    ('ล้านล้าน', 'สิบล้านล้าน', 'ร้อยล้านล้าน'),
    ('พันล้านล้าน', 'หมื่นล้านล้าน', 'แสนล้านล้าน'),
    ('ล้านล้านล้าน', 'สิบล้านล้านล้าน', 'ร้อยล้านล้านล้าน'),
    ('พันล้านล้านล้าน', 'หมื่นล้านล้านล้าน', 'แสนล้านล้านล้าน'),
    ('ล้านล้านล้านล้าน', 'สิบล้านล้านล้านล้าน', 'ร้อยล้านล้านล้านล้าน'),
    ('พันล้านล้านล้านล้าน', 'หมื่นล้านล้านล้านล้าน', 'แสนล้านล้านล้านล้าน'),
    ('ล้านล้านล้านล้านล้าน', 'สิบล้านล้านล้านล้านล้าน', 'ร้อยล้านล้านล้านล้านล้าน'),
]

_fractions = {
    2: 'ครึ่ง',
    3: 'หนึ่งในสาม',
    4: 'หนึ่งในสี่',
    5: 'หนึ่งในห้า',
    6: 'หนึ่งในหก',
    7: 'หนึ่งในเจ็ด',
    8: 'หนึ่งในแปด',
    9: 'หนึ่งในเก้า',
    10: 'หนึ่งในสิบ',
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
            return _tens[tens] + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if number == 1:
        return _scales[scale_index][0]
    elif number == 2:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words}จุด{fraction_words}"

    if number == 0:
        return 'ศูนย์'

    if number < 0:
        return 'ลบ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ''.join(reversed(parts))