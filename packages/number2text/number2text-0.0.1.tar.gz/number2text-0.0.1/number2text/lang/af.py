_ones = ["", "een", "twee", "drie", "vier", "vyf", "ses", "sewe", "agt", "nege"]
_teens = ["tien", "elf", "twaalf", "dertien", "veertien", "vyftien", "sestien", "sewentien", "agtien", "negentien"]
_tens = ["", "", "twintig", "dertig", "veertig", "vyftig", "sestig", "sewentig", "tagtig", "negentig"]
_hundreds = ["", "eenhonderd", "tweehonderd", "driehonderd", "vierhonderd", "vyfhonderd", "seshonderd", "sewehonderd", "agthonderd", "negehonderd"]

_scales = [
    ("", "", ""),
    ("duisend", "duisend", "duisend"),
    ("miljoen", "miljoen", "miljoen"),
    ("miljard", "miljard", "miljard"),
    ("biljoen", "biljoen", "biljoen"),
    ("biljard", "biljard", "biljard"),
    ("triljoen", "triljoen", "triljoen"),
    ("triljard", "triljard", "triljard"),
    ("kwadriljoen", "kwadriljoen", "kwadriljoen"),
    ("kwadriljard", "kwadriljard", "kwadriljard"),
    ("kwintiljoen", "kwintiljoen", "kwintiljoen"),
    ("kwintiljard", "kwintiljard", "kwintiljard"),
]

_fractions = {
    2: 'halwe',
    3: 'derde',
    4: 'kwart',
    5: 'vyfde',
    6: 'sesde',
    7: 'sewende',
    8: 'agtste',
    9: 'negende',
    10: 'tiende',
}

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    else:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + "-en-" + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + "-en-" + convert_less_than_hundred(less_than_hundred)

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
        return convert(numerator) + " " + _fractions[denominator] + ("s" if numerator > 1 else "")

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
        return "minus " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                if scale_index > 0 and number % 1000 < 100:
                    part = "en-" + part
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))