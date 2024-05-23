_ones= ["", "een", "twee", "drie", "vier", "vijf", "zes", "zeven", "acht", "negen"]
_teens = ["tien", "elf", "twaalf", "dertien", "veertien", "vijftien", "zestien", "zeventien", "achttien", "negentien"]
_tens = ["", "", "twintig", "dertig", "veertig", "vijftig", "zestig", "zeventig", "tachtig", "negentig"]
_hundreds = ["", "honderd", "tweehonderd", "driehonderd", "vierhonderd", "vijfhonderd", "zeshonderd", "zevenhonderd", "achthonderd", "negenhonderd"]

_scales = [
    ("", "", ""),
    ("duizend", "duizend", "duizend"),
    ("miljoen", "miljoen", "miljoen"),
    ("miljard", "miljard", "miljard"),
    ("biljoen", "biljoen", "biljoen"),
    ("biljard", "biljard", "biljard"),
    ("triljoen", "triljoen", "triljoen"),
    ("triljard", "triljard", "triljard"),
    ("quadriljoen", "quadriljoen", "quadriljoen"),
    ("quadriljard", "quadriljard", "quadriljard"),
    ("quintiljoen", "quintiljoen", "quintiljoen"),
    ("quintiljard", "quintiljard", "quintiljard"),
]

_fractions = {
    2: 'half',
    3: 'derde',
    4: 'vierde',
    5: 'vijfde',
    6: 'zesde',
    7: 'zevende',
    8: 'achtste',
    9: 'negende',
    10: 'tiende',
}

def convert_less_than_hundred(number):
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

def convert_less_than_thousand(number):
    hundreds, less_than_hundred = divmod(number, 100)
    if hundreds == 0:
        return convert_less_than_hundred(less_than_hundred)
    elif less_than_hundred == 0:
        return _hundreds[hundreds]
    else:
        return _hundreds[hundreds] + convert_less_than_hundred(less_than_hundred)

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

        return f"{integer_words} komma {fraction_words}"

    if number == 0:
        return "nul"

    if number < 0:
        return "min " + convert(-number)

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