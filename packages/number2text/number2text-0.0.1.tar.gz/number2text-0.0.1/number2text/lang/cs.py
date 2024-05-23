_ones= ["", "jedna", "dvě", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
_teens = ["deset", "jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
_tens = ["", "", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
_hundreds = ["", "sto", "dvě stě", "tři sta", "čtyři sta", "pět set", "šest set", "sedm set", "osm set", "devět set"]

_scales = [
    ("", "", ""),
    ("tisíc", "tisíce", "tisíc"),
    ("milion", "miliony", "milionů"),
    ("miliarda", "miliardy", "miliard"),
    ("bilion", "biliony", "bilionů"),
    ("biliarda", "biliardy", "biliard"),
    ("trilion", "triliony", "trilionů"),
    ("triliarda", "triliardy", "triliard"),
    ("kvadrilion", "kvadriliony", "kvadrilionů"),
    ("kvadriliarda", "kvadriliardy", "kvadriliard"),
]

_fractions = {
    2: "polovina",
    3: "třetina",
    4: "čtvrtina",
    5: "pětina",
    6: "šestina",
    7: "sedmina",
    8: "osmina",
    9: "devítina",
    10: "desetina",
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