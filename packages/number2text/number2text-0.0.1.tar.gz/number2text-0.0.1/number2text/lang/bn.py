_ones= ["", "এক", "দুই", "তিন", "চার", "পাঁচ", "ছয়", "সাত", "আট", "নয়"]
_teens = ["দশ", "এগারো", "বারো", "তেরো", "চৌদ্দ", "পনেরো", "ষোল", "সতেরো", "আঠারো", "উনিশ"]
_tens = ["", "", "বিশ", "ত্রিশ", "চল্লিশ", "পঞ্চাশ", "ষাট", "সত্তর", "আশি", "নব্বই"]
_hundreds = ["", "একশো", "দুইশো", "তিনশো", "চারশো", "পাঁচশো", "ছয়শো", "সাতশো", "আটশো", "নয়শো"]

_scales = [
    ("", "", ""),
    ("হাজার", "হাজার", "হাজার"),
    ("লক্ষ", "লক্ষ", "লক্ষ"),
    ("কোটি", "কোটি", "কোটি"),
    ("শত কোটি", "শত কোটি", "শত কোটি"),
    ("হাজার কোটি", "হাজার কোটি", "হাজার কোটি"),
    ("লক্ষ কোটি", "লক্ষ কোটি", "লক্ষ কোটি"),
    ("কোটি কোটি", "কোটি কোটি", "কোটি কোটি"),
    ("শত কোটি কোটি", "শত কোটি কোটি", "শত কোটি কোটি"),
    ("হাজার কোটি কোটি", "হাজার কোটি কোটি", "হাজার কোটি কোটি"),
    ("লক্ষ কোটি কোটি", "লক্ষ কোটি কোটি", "লক্ষ কোটি কোটি"),
]

_fractions = {
    2: 'অর্ধেক',
    3: 'এক তৃতীয়াংশ',
    4: 'এক চতুর্থাংশ',
    5: 'এক পঞ্চমাংশ',
    6: 'এক ষষ্ঠাংশ',
    7: 'এক সপ্তমাংশ',
    8: 'এক অষ্টমাংশ',
    9: 'এক নবমাংশ',
    10: 'এক দশমাংশ',
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
    elif number > 1:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

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

        return f"{integer_words} দশমিক {fraction_words}"

    if number == 0:
        return "শূন্য"

    if number < 0:
        return "ঋণাত্মক " + convert(-number)

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