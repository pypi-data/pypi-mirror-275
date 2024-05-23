_ones= ["", "ọkan", "meji", "mẹta", "mẹrin", "marun", "mẹfa", "meje", "mẹjọ", "mẹsan"]
_teens = ["mẹwa", "mọkanla", "mejila", "mẹtala", "mẹrinla", "mẹẹdogun", "mẹrindilogun", "mẹtadilogun", "mejidinlogun", "okandinlogun"]
_tens = ["", "", "ogun", "ọgbọn", "ogoji", "aadọta", "ọgọta", "aadọrin", "ọgọrin", "aadọrun"]
_hundreds = ["", "ọgọrun", "igba", "ọ̀ọ́dúrún", "irinwó", "ẹdẹgbẹta", "ẹgbẹta", "ẹẹdẹgbẹrin", "ẹgbẹ̀rin", "ẹ̀ẹ́dẹ́gbẹ́rún"]

_scales = [
    ("", "", ""),
    ("ẹgbẹrun", "ẹgbẹrun", "ẹgbẹrun"),
    ("miliọnu", "miliọnu", "miliọnu"),
    ("biliọnu", "biliọnu", "biliọnu"),
    ("tiriliọnu", "tiriliọnu", "tiriliọnu"),
    ("kuadiriliọnu", "kuadiriliọnu", "kuadiriliọnu"),
    ("kuintiriliọnu", "kuintiriliọnu", "kuintiriliọnu"),
    ("sẹstiriliọnu", "sẹstiriliọnu", "sẹstiriliọnu"),
    ("sẹptiriliọnu", "sẹptiriliọnu", "sẹptiriliọnu"),
    ("ọktiriliọnu", "ọktiriliọnu", "ọktiriliọnu"),
    ("nọniriliọnu", "nọniriliọnu", "nọniriliọnu"),
    ("dẹsiriliọnu", "dẹsiriliọnu", "dẹsiriliọnu"),
]

_fractions = {
    2: 'idaji',
    3: 'idamẹta',
    4: 'idamẹrin',
    5: 'idamarun',
    6: 'idamẹfa',
    7: 'idameje',
    8: 'idamẹjọ',
    9: 'idamẹsan',
    10: 'idamẹwa',
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

        return f"{integer_words} ati {fraction_words}"

    if number == 0:
        return "ọdọ"

    if number < 0:
        return "din " + convert(-number)

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