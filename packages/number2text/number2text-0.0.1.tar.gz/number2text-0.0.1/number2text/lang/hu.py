_ones= ["", "egy", "kettő", "három", "négy", "öt", "hat", "hét", "nyolc", "kilenc"]
_teens = ["tíz", "tizenegy", "tizenkettő", "tizenhárom", "tizennégy", "tizenöt", "tizenhat", "tizenhét", "tizennyolc", "tizenkilenc"]
_tens = ["", "", "húsz", "harminc", "negyven", "ötven", "hatvan", "hetven", "nyolcvan", "kilencven"]
_hundreds = ["", "száz", "kétszáz", "háromszáz", "négyszáz", "ötszáz", "hatszáz", "hétszáz", "nyolcszáz", "kilencszáz"]

_scales = [
    ("", "", ""),
    ("ezer", "ezer", "ezer"),
    ("millió", "millió", "millió"),
    ("milliárd", "milliárd", "milliárd"),
    ("billió", "billió", "billió"),
    ("billiárd", "billiárd", "billiárd"),
    ("trillió", "trillió", "trillió"),
    ("trilliárd", "trilliárd", "trilliárd"),
    ("kvadrillió", "kvadrillió", "kvadrillió"),
    ("kvadrilliárd", "kvadrilliárd", "kvadrilliárd"),
    ("kvintillió", "kvintillió", "kvintillió"),
    ("kvintilliárd", "kvintilliárd", "kvintilliárd"),
]

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
            return _tens[tens] + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_hundred(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif number == 0:
        return _scales[scale_index][2]
    else:
        return _scales[scale_index][1]

def convert(number):
    if number == 0:
        return "nulla"

    if number < 0:
        return "mínusz " + convert(-number)

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