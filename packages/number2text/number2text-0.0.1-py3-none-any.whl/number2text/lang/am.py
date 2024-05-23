_ones= ["", "yek", "do", "se", "chahār", "panj", "shesh", "haft", "hasht", "noh"]
_teens = ["dah", "yāzdah", "davāzdah", "sizdah", "chahārdah", "pānzdah", "shānzdah", "hefdah", "hejdah", "noozdah"]
_tens = ["", "", "bist", "si", "chehel", "panjāh", "shast", "haftād", "hashtād", "navad"]
_hundreds = ["", "sad", "devist", "sisad", "chahārsad", "pānsad", "sheshsad", "haftsad", "hashtsad", "nohsad"]

_scales = [
    ("", "", ""),
    ("hezār", "hezār", "hezār"),
    ("milion", "milion", "milion"),
    ("miliārd", "miliārd", "miliārd"),
    ("bilion", "bilion", "bilion"),
    ("biliārd", "biliārd", "biliārd"),
    ("tilion", "tilion", "tilion"),
    ("tiliārd", "tiliārd", "tiliārd"),
    ("katrilion", "katrilion", "katrilion"),
    ("katriliārd", "katriliārd", "katriliārd"),
    ("kentilion", "kentilion", "kentilion"),
    ("kentiliārd", "kentiliārd", "kentiliārd"),
]

_fractions = {
    2: 'nim',
    3: 'yek sevvom',
    4: 'yek chahārom',
    5: 'yek panjom',
    6: 'yek sheshom',
    7: 'yek haftom',
    8: 'yek hashtom',
    9: 'yek nohom',
    10: 'yek dahom',
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
            return _tens[tens] + " o " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " o " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} va {fraction_words}"

    if number == 0:
        return "sefr"

    if number < 0:
        return "manfi " + convert(-number)

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

    return " o ".join(reversed(parts))