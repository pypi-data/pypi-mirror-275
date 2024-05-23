_ones= ["", "یک", "دو", "سه", "چهار", "پنج", "شش", "هفت", "هشت", "نه"]
_teens = ["ده", "یازده", "دوازده", "سیزده", "چهارده", "پانزده", "شانزده", "هفده", "هجده", "نوزده"]
_tens = ["", "", "بیست", "سی", "چهل", "پنجاه", "شصت", "هفتاد", "هشتاد", "نود"]
_hundreds = ["", "صد", "دویست", "سیصد", "چهارصد", "پانصد", "ششصد", "هفتصد", "هشتصد", "نهصد"]

_scales = [
    ("", "", ""),
    ("هزار", "هزار", "هزار"),
    ("میلیون", "میلیون", "میلیون"),
    ("میلیارد", "میلیارد", "میلیارد"),
    ("تریلیون", "تریلیون", "تریلیون"),
    ("کوادریلیون", "کوادریلیون", "کوادریلیون"),
    ("کوینتیلیون", "کوینتیلیون", "کوینتیلیون"),
    ("سکستیلیون", "سکستیلیون", "سکستیلیون"),
    ("سپتیلیون", "سپتیلیون", "سپتیلیون"),
    ("اکتیلیون", "اکتیلیون", "اکتیلیون"),
    ("نونیلیون", "نونیلیون", "نونیلیون"),
    ("دسیلیون", "دسیلیون", "دسیلیون"),
]

_fractions = {
    2: 'نیم',
    3: 'ثلث',
    4: 'ربع',
    5: 'خمس',
    6: 'سدس',
    7: 'سبع',
    8: 'ثمن',
    9: 'تسع',
    10: 'عشر',
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
            return _tens[tens] + " و " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " و " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} ممیز {fraction_words}"

    if number == 0:
        return "صفر"

    if number < 0:
        return "منفی " + convert(-number)

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

    return " و ".join(reversed(parts))