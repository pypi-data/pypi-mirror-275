_ones= ["", "otu", "abuo", "ato", "ano", "ise", "isii", "asaa", "asato", "itoolu"]
_teens = ["iri", "iri na otu", "iri na abuo", "iri na ato", "iri na ano", "iri na ise", "iri na isii", "iri na asaa", "iri na asato", "iri na itoolu"]
_tens = ["", "", "ogu", "ogu na", "ogu abuo", "ogu ato", "ogu ano", "ogu ise", "ogu isii", "ogu asaa"]
_hundreds = ["", "nari", "nari abuo", "nari ato", "nari ano", "nari ise", "nari isii", "nari asaa", "nari asato", "nari itoolu"]

_scales = [
    ("", "", ""),
    ("puku", "puku", "puku"),
    ("nde", "nde", "nde"),
    ("ijeri", "ijeri", "ijeri"),
    ("bilion", "bilion", "bilion"),
    ("bilion nari", "bilion nari", "bilion nari"),
    ("trilion", "trilion", "trilion"),
    ("trilion nari", "trilion nari", "trilion nari"),
    ("kuadirilion", "kuadirilion", "kuadirilion"),
    ("kuadirilion nari", "kuadirilion nari", "kuadirilion nari"),
    ("kuintilion", "kuintilion", "kuintilion"),
    ("kuintilion nari", "kuintilion nari", "kuintilion nari"),
]

_fractions = {
    2: 'oke',
    3: 'oke ato',
    4: 'oke ano',
    5: 'oke ise',
    6: 'oke isii',
    7: 'oke asaa',
    8: 'oke asato',
    9: 'oke itoolu',
    10: 'oke iri',
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
            return _tens[tens] + " na " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " na " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} na {fraction_words}"

    if number == 0:
        return "efuo"

    if number < 0:
        return "erughachi " + convert(-number)

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