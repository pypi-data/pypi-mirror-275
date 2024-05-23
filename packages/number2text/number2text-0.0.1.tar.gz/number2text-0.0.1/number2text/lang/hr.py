_ones= ["", "jedan", "dva", "tri", "četiri", "pet", "šest", "sedam", "osam", "devet"]
_teens = ["deset", "jedanaest", "dvanaest", "trinaest", "četrnaest", "petnaest", "šesnaest", "sedamnaest", "osamnaest", "devetnaest"]
_tens = ["", "", "dvadeset", "trideset", "četrdeset", "pedeset", "šezdeset", "sedamdeset", "osamdeset", "devedeset"]
_hundreds = ["", "sto", "dvjesto", "tristo", "četiristo", "petsto", "šesto", "sedamsto", "osamsto", "devetsto"]

_scales = [
    ("", "", ""),
    ("tisuća", "tisuće", "tisuća"),
    ("milijun", "milijuna", "milijuna"),
    ("milijarda", "milijarde", "milijardi"),
    ("bilijun", "bilijuna", "bilijuna"),
    ("bilijarda", "bilijarde", "bilijardi"),
    ("trilijun", "trilijuna", "trilijuna"),
    ("trilijarda", "trilijarde", "trilijardi"),
    ("kvadrilijun", "kvadrilijuna", "kvadrilijuna"),
    ("kvadrilijarda", "kvadrilijarde", "kvadrilijardi"),
]

_fractions = {
    2: "polovina",
    3: "trećina",
    4: "četvrtina",
    5: "petina",
    6: "šestina",
    7: "sedmina",
    8: "osmina",
    9: "devetina",
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

        return f"{integer_words} i {fraction_words}"

    if number == 0:
        return "nula"

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