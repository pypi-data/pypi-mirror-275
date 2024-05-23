_ones= ["", "en", "to", "tre", "fire", "fem", "seks", "syv", "otte", "ni"]
_teens = ["ti", "elleve", "tolv", "tretten", "fjorten", "femten", "seksten", "sytten", "atten", "nitten"]
_tens = ["", "", "tyve", "tredive", "fyrre", "halvtreds", "tres", "halvfjerds", "firs", "halvfems"]
_hundreds = ["", "et hundrede", "to hundrede", "tre hundrede", "fire hundrede", "fem hundrede", "seks hundrede", "syv hundrede", "otte hundrede", "ni hundrede"]

_scales = [
    ("", "", ""),
    ("tusind", "tusind", "tusind"),
    ("million", "millioner", "millioner"),
    ("milliard", "milliarder", "milliarder"),
    ("billion", "billioner", "billioner"),
    ("billiard", "billiarder", "billiarder"),
    ("trillion", "trillioner", "trillioner"),
    ("trilliard", "trilliarder", "trilliarder"),
    ("kvadrillion", "kvadrillioner", "kvadrillioner"),
    ("kvadrilliard", "kvadrilliarder", "kvadrilliarder"),
    ("kvintillion", "kvintillioner", "kvintillioner"),
    ("kvintilliard", "kvintilliarder", "kvintilliarder"),
]

_fractions = {
    2: 'halv',
    3: 'tredjedel',
    4: 'fjerdedel',
    5: 'femtedel',
    6: 'sjettedel',
    7: 'syvendedel',
    8: 'ottendedel',
    9: 'niendedel',
    10: 'tiendedel',
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
        elif ones == 1:
            return _tens[tens][:-1] + "en"
        else:
            return _tens[tens] + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        elif hundreds == 1:
            return "et hundrede og " + convert_less_than_hundred(less_than_hundred)
        else:
            return _hundreds[hundreds] + " og " + convert_less_than_hundred(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif 1 < number < 10:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator] + "e"

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
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))