_ones= ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
_teens = ["mười", "mười một", "mười hai", "mười ba", "mười bốn", "mười lăm", "mười sáu", "mười bảy", "mười tám", "mười chín"]
_tens = ["", "", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
_hundreds = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm", "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]

_scales = [
    ("", "", ""),
    ("nghìn", "nghìn", "nghìn"),
    ("triệu", "triệu", "triệu"),
    ("tỷ", "tỷ", "tỷ"),
    ("nghìn tỷ", "nghìn tỷ", "nghìn tỷ"),
    ("triệu tỷ", "triệu tỷ", "triệu tỷ"),
    ("tỷ tỷ", "tỷ tỷ", "tỷ tỷ"),
    ("nghìn tỷ tỷ", "nghìn tỷ tỷ", "nghìn tỷ tỷ"),
    ("triệu tỷ tỷ", "triệu tỷ tỷ", "triệu tỷ tỷ"),
    ("tỷ tỷ tỷ", "tỷ tỷ tỷ", "tỷ tỷ tỷ"),
    ("nghìn tỷ tỷ tỷ", "nghìn tỷ tỷ tỷ", "nghìn tỷ tỷ tỷ"),
    ("triệu tỷ tỷ tỷ", "triệu tỷ tỷ tỷ", "triệu tỷ tỷ tỷ"),
]

_fractions = {
    2: 'một nửa',
    3: 'một phần ba',
    4: 'một phần tư',
    5: 'một phần năm',
    6: 'một phần sáu',
    7: 'một phần bảy',
    8: 'một phần tám',
    9: 'một phần chín',
    10: 'một phần mười',
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
            return _tens[tens] + " " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    else:
        return _scales[scale_index][1]

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

        return f"{integer_words} phẩy {fraction_words}"

    if number == 0:
        return "không"

    if number < 0:
        return "âm " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))