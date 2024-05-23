_ones= ["", "មួយ", "ពីរ", "បី", "បួន", "ប្រាំ", "ប្រាំមួយ", "ប្រាំពីរ", "ប្រាំបី", "ប្រាំបួន"]
_teens = ["ដប់", "ដប់មួយ", "ដប់ពីរ", "ដប់បី", "ដប់បួន", "ដប់ប្រាំ", "ដប់ប្រាំមួយ", "ដប់ប្រាំពីរ", "ដប់ប្រាំបី", "ដប់ប្រាំបួន"]
_tens = ["", "", "ម្ភៃ", "សាមសិប", "សែសិប", "ហាសិប", "ហុកសិប", "ចិតសិប", "ប៉ែតសិប", "កៅសិប"]
_hundreds = ["", "មួយរយ", "ពីររយ", "បីរយ", "បួនរយ", "ប្រាំរយ", "ប្រាំមួយរយ", "ប្រាំពីររយ", "ប្រាំបីរយ", "ប្រាំបួនរយ"]

_scales = [
    ("", "", ""),
    ("ពាន់", "ពាន់", "ពាន់"),
    ("លាន", "លាន", "លាន"),
    ("ប៊ីលាន", "ប៊ីលាន", "ប៊ីលាន"),
    ("ទ្រីលាន", "ទ្រីលាន", "ទ្រីលាន"),
    ("ក្វាទ្រីលាន", "ក្វាទ្រីលាន", "ក្វាទ្រីលាន"),
    ("ក្វីនទីលាន", "ក្វីនទីលាន", "ក្វីនទីលាន"),
    ("សិចទីលាន", "សិចទីលាន", "សិចទីលាន"),
    ("សិបទីលាន", "សិបទីលាន", "សិបទីលាន"),
    ("អុកតីលាន", "អុកតីលាន", "អុកតីលាន"),
    ("ណូនីលាន", "ណូនីលាន", "ណូនីលាន"),
    ("ដេស៊ីលាន", "ដេស៊ីលាន", "ដេស៊ីលាន"),
]

_fractions = {
    2: 'ពាក់កណ្ដាល',
    3: 'ភាគបី',
    4: 'ភាគបួន',
    5: 'ភាគប្រាំ',
    6: 'ភាគប្រាំមួយ',
    7: 'ភាគប្រាំពីរ',
    8: 'ភាគប្រាំបី',
    9: 'ភាគប្រាំបួន',
    10: 'ភាគដប់',
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
        return convert(numerator) + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} ក្បៀស {fraction_words}"

    if number == 0:
        return "សូន្យ"

    if number < 0:
        return "ដក " + convert(-number)

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

    return "".join(reversed(parts))