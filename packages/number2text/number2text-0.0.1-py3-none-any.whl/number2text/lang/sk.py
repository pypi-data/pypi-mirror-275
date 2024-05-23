_ones= ["", "jeden", "dva", "tri", "štyri", "päť", "šesť", "sedem", "osem", "deväť"]
_teens = ["desať", "jedenásť", "dvanásť", "trinásť", "štrnásť", "pätnásť", "šestnásť", "sedemnásť", "osemnásť", "devätnásť"]
_tens = ["", "", "dvadsať", "tridsať", "štyridsať", "päťdesiat", "šesťdesiat", "sedemdesiat", "osemdesiat", "deväťdesiat"]
_hundreds = ["", "sto", "dvesto", "tristo", "štyristo", "päťsto", "šesťsto", "sedemsto", "osemsto", "deväťsto"]

_scales = [
    ("", "", ""),
    ("tisíc", "tisíce", "tisíc"),
    ("milión", "milióny", "miliónov"),
    ("miliarda", "miliardy", "miliárd"),
    ("bilión", "bilióny", "biliónov"),
    ("biliarda", "biliardy", "biliárd"),
    ("trilión", "trilióny", "triliónov"),
    ("triliarda", "triliardy", "triliárd"),
    ("kvadrilión", "kvadrilióny", "kvadriliónov"),
    ("kvadriliarda", "kvadriliardy", "kvadriliárd"),
]

_fractions = {
    2: "polovica",
    3: "tretina",
    4: "štvrtina",
    5: "pätina",
    6: "šestina",
    7: "sedmina",
    8: "osmina",
    9: "devätina",
    10: "desatina",
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
    elif 2 <= number <= 4:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

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

        return f"{integer_words} a {fraction_words}"

    if number == 0:
        return "nula"

    if number < 0:
        return "mínus " + convert(-number)

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