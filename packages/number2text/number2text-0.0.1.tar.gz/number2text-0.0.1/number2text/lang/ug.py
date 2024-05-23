_ones= ["", "bir", "ikki", "üç", "tört", "bäş", "alte", "yette", "sekkiz", "toqquz"]
_teens = ["on", "on bir", "on ikki", "on üç", "on tört", "on bäş", "on alte", "on yette", "on sekkiz", "on toqquz"]
_tens = ["", "", "yigirme", "otuz", "qirq", "ällik", "atmish", "yätmish", "säksän", "toqsan"]
_hundreds = ["", "bir yüz", "ikki yüz", "üç yüz", "tört yüz", "bäş yüz", "alte yüz", "yette yüz", "sekkiz yüz", "toqquz yüz"]

_scales = [
    ("", "", ""),
    ("ming", "ming", "ming"),
    ("million", "million", "million"),
    ("milliard", "milliard", "milliard"),
    ("trillion", "trillion", "trillion"),
    ("kvadrillion", "kvadrillion", "kvadrillion"),
    ("kvintilion", "kvintilion", "kvintilion"),
    ("sekstilion", "sekstilion", "sekstilion"),
    ("septilion", "septilion", "septilion"),
    ("oktilion", "oktilion", "oktilion"),
    ("nonilion", "nonilion", "nonilion"),
    ("detsillion", "detsillion", "detsillion"),
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
    else:
        return _scales[scale_index][1]

def convert(number):
    if number == 0:
        return "nol"

    if number < 0:
        return "minus " + convert(-number)

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