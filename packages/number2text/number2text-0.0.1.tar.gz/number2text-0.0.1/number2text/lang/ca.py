_ones= ["", "u", "dos", "tres", "quatre", "cinc", "sis", "set", "vuit", "nou"]
_teens = ["deu", "onze", "dotze", "tretze", "catorze", "quinze", "setze", "disset", "divuit", "dinou"]
_tens = ["", "", "vint", "trenta", "quaranta", "cinquanta", "seixanta", "setanta", "vuitanta", "noranta"]
_hundreds = ["", "cent", "dos-cents", "tres-cents", "quatre-cents", "cinc-cents", "sis-cents", "set-cents", "vuit-cents", "nou-cents"]

_scales = [
    ("", "", ""),
    ("mil", "mil", "mil"),
    ("milió", "milions", "milions"),
    ("miliard", "miliards", "miliards"),
    ("bilió", "bilions", "bilions"),
    ("biliard", "biliards", "biliards"),
    ("trilió", "trilions", "trilions"),
    ("triliard", "triliards", "triliards"),
    ("quadrilió", "quadrilions", "quadrilions"),
    ("quadriliard", "quadriliards", "quadriliards"),
    ("quintilió", "quintilions", "quintilions"),
    ("quintiliard", "quintiliards", "quintiliards"),
]

def convert_less_than_thousand(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        elif tens == 0:
            return _ones[ones]
        else:
            return _tens[tens] + "-" + _ones[ones]
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
    elif number == 0:
        return ""
    else:
        return _scales[scale_index][1] if 1 < number < 2 else _scales[scale_index][2]

def convert(number):
    if number == 0:
        return "zero"

    if number < 0:
        return "menys " + convert(-number)

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