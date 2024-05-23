_ones= ["", "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän"]
_teens = ["kymmenen", "yksitoista", "kaksitoista", "kolmetoista", "neljätoista", "viisitoista", "kuusitoista", "seitsemäntoista", "kahdeksantoista", "yhdeksäntoista"]
_tens = ["", "", "kaksikymmentä", "kolmekymmentä", "neljäkymmentä", "viisikymmentä", "kuusikymmentä", "seitsemänkymmentä", "kahdeksankymmentä", "yhdeksänkymmentä"]
_hundreds = ["", "sata", "kaksisataa", "kolmesataa", "neljäsataa", "viisisataa", "kuusisataa", "seitsemänsataa", "kahdeksansataa", "yhdeksänsataa"]

_scales = [
    ("", "", ""),
    ("tuhat", "tuhatta", "tuhatta"),
    ("miljoona", "miljoonaa", "miljoonaa"),
    ("miljardi", "miljardia", "miljardia"),
    ("biljoona", "biljoonaa", "biljoonaa"),
    ("kvadriljoona", "kvadriljoonaa", "kvadriljoonaa"),
    ("kvintiljoona", "kvintiljoonaa", "kvintiljoonaa"),
    ("sekstiljoona", "sekstiljoonaa", "sekstiljoonaa"),
    ("septiljoona", "septiljoonaa", "septiljoonaa"),
    ("oktiljoona", "oktiljoonaa", "oktiljoonaa"),
    ("noniljoona", "noniljoonaa", "noniljoonaa"),
    ("dekiljoona", "dekiljoonaa", "dekiljoonaa"),
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
    else:
        return _scales[scale_index][1]

def convert(number):
    if number == 0:
        return "nolla"

    if number < 0:
        return "miinus " + convert(-number)

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