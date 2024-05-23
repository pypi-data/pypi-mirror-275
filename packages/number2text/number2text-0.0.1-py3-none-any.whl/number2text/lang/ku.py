_ones= ["", "yek", "du", "sê", "çar", "pênc", "şeş", "heft", "heşt", "neh"]
_teens = ["deh", "yazdeh", "duwazdeh", "sêzdeh", "çardeh", "panzdeh", "şazdeh", "hevdeh", "hejdeh", "nozdeh"]  
_tens = ["", "", "bîst", "sî", "çil", "pêncî", "şêst", "heftê", "heştê", "nod"]
_hundreds = ["", "sed", "dused", "sêsed", "çarsed", "pêncsed", "şeşsed", "heftsed", "heştsed", "nehsed"]

_scales = [
    ("", "", ""),
    ("hezar", "hezar", "hezar"),
    ("milyon", "milyon", "milyon"),
    ("milyar", "milyar", "milyar"),
    ("trilyon", "trilyon", "trilyon"),
    ("katrilyon", "katrilyon", "katrilyon"),
    ("kentilyon", "kentilyon", "kentilyon"),
    ("sekstilyon", "sekstilyon", "sekstilyon"),
    ("septilyon", "septilyon", "septilyon"),
    ("oktilyon", "oktilyon", "oktilyon"),
    ("nonilyon", "nonilyon", "nonilyon"),
    ("desilyon", "desilyon", "desilyon"),
]

_fractions = {
    2: 'nîv',
    3: 'sêyek',
    4: 'çaryek', 
    5: 'pêncyek',
    6: 'şeşyek',
    7: 'heftyek',
    8: 'heştyek',
    9: 'nehyek',
    10: 'dehyek',
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
            return _tens[tens] + " û " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " û " + convert_less_than_thousand(less_than_hundred)

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
        return convert(numerator) + "yekî " + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} û {fraction_words}"

    if number == 0:
        return "sifir"

    if number < 0:
        return "negatîf " + convert(-number)

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