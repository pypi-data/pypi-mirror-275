_ones= ["", "viens", "divi", "trīs", "četri", "pieci", "seši", "septiņi", "astoņi", "deviņi"]
_teens = ["desmit", "vienpadsmit", "divpadsmit", "trīspadsmit", "četrpadsmit", "piecpadsmit", "sešpadsmit", "septiņpadsmit", "astoņpadsmit", "deviņpadsmit"]
_tens = ["", "", "divdesmit", "trīsdesmit", "četrdesmit", "piecdesmit", "sešdesmit", "septiņdesmit", "astoņdesmit", "deviņdesmit"]
_hundreds = ["", "simts", "divsimt", "trīssimt", "četrsimt", "piecsimt", "sešsimt", "septiņsimt", "astoņsimt", "deviņsimt"]

_scales = [
    ("", "", ""),
    ("tūkstotis", "tūkstoši", "tūkstošu"),
    ("miljons", "miljoni", "miljonu"),
    ("miljards", "miljardi", "miljardu"),
    ("triljons", "triljoni", "triljonu"),
    ("kvadriljons", "kvadriljoni", "kvadriljonu"),
    ("kvintiljons", "kvintiljoni", "kvintiljonu"),
    ("sekstiljons", "sekstiljoni", "sekstiljonu"),
    ("septiljons", "septiljoni", "septiljonu"),
    ("oktiljons", "oktiljoni", "oktiljonu"),
    ("noniljons", "noniljoni", "noniljonu"),
    ("deciljons", "deciljoni", "deciljonu"),
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
    elif 1 < number < 10:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert(number):
    if number == 0:
        return "nulle"

    if number < 0:
        return "mīnus " + convert(-number)

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