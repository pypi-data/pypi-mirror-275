_ones= ["", "bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]
_teens = ["on", "on bir", "on iki", "on üç", "on dörd", "on beş", "on altı", "on yeddi", "on səkkiz", "on doqquz"]
_tens = ["", "", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doxsan"]
_hundreds = ["", "yüz", "iki yüz", "üç yüz", "dörd yüz", "beş yüz", "altı yüz", "yeddi yüz", "səkkiz yüz", "doqquz yüz"]

_scales = [
    ("", "", ""),
    ("min", "min", "min"),
    ("milyon", "milyon", "milyon"),
    ("milyard", "milyard", "milyard"),
    ("trilyon", "trilyon", "trilyon"),
    ("kvadrilyon", "kvadrilyon", "kvadrilyon"),
    ("kvintilyon", "kvintilyon", "kvintilyon"),
    ("sekstilyon", "sekstilyon", "sekstilyon"),
    ("septilyon", "septilyon", "septilyon"),
    ("oktilyon", "oktilyon", "oktilyon"),
    ("nonilyon", "nonilyon", "nonilyon"),
    ("desilyon", "desilyon", "desilyon"),
]

_fractions = {
    2: 'yarım',
    3: 'üçdə bir',
    4: 'dörddə bir',
    5: 'beşdə bir',
    6: 'altıda bir',
    7: 'yeddidə bir',
    8: 'səkkizdə bir',
    9: 'doqquzda bir',
    10: 'onda bir',
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

        return f"{integer_words} tam {fraction_words}"

    if number == 0:
        return "sıfır"

    if number < 0:
        return "mənfi " + convert(-number)

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