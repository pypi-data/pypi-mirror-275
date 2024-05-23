_ones= ["", "eden", "dva", "tri", "chetiri", "pet", "shest", "sedum", "osum", "devet"]
_teens = ["deset", "edinaeset", "dvanaeset", "trinaeset", "chetirineset", "petneset", "shesnaeset", "sedumnaeset", "osumnaeset", "devetnaeset"]  
_tens = ["", "", "dvaeset", "trieset", "chetirineset", "pedeset", "sheeeset", "sedumdeset", "osumdeset", "devedeset"]
_hundreds = ["", "sto", "dveste", "trista", "chetiristotini", "petstotini", "sheststotini", "sedumstotini", "osumstotini", "devetstotini"]

_scales = [
    ("", "", ""),
    ("iljada", "iljadi", "iljadi"),
    ("milion", "milioni", "milioni"), 
    ("milijarda", "milijardi", "milijardi"),
    ("bilion", "bilioni", "bilioni"),
    ("bilijarda", "bilijardi", "bilijardi"),
    ("trilion", "trilioni", "trilioni"),
    ("trilijarda", "trilijardi", "trilijardi"),
    ("kvadrilion", "kvadrilioni", "kvadrilioni"),
    ("kvadrilijarda", "kvadrilijardi", "kvadrilijardi"),
    ("kvintilion", "kvintilioni", "kvintilioni"),
    ("kvintilijarda", "kvintilijardi", "kvintilijardi"),
]

_fractions = {
    2: 'polovina',
    3: 'tretina',
    4: 'chetvrtina', 
    5: 'petina',
    6: 'shestina',
    7: 'sedmina',
    8: 'osmina',
    9: 'devetina',
    10: 'desetina',
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
            return _tens[tens] + " i " + _ones[ones]
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
    elif number % 10 == 1:
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