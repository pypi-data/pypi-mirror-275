_ones = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove"]
_teens = ["dieci", "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove"]
_tens = ["", "", "venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
_hundreds = ["", "cento", "duecento", "trecento", "quattrocento", "cinquecento", "seicento", "settecento", "ottocento", "novecento"]

_scales = [
    ("", "", ""),
    ("mille", "mila", "mila"),
    ("milione", "milioni", "milioni"),
    ("miliardo", "miliardi", "miliardi"),
    ("bilione", "bilioni", "bilioni"),
    ("biliardo", "biliardi", "biliardi"),
    ("trilione", "trilioni", "trilioni"),
    ("triliardo", "triliardi", "triliardi"),
    ("quadrilione", "quadrilioni", "quadrilioni"),
    ("quadriliardo", "quadriliardi", "quadriliardi"),
    ("quintilione", "quintilioni", "quintilioni"),
    ("quintiliardo", "quintiliardi", "quintiliardi"),
]

_fractions = {
    2: 'mezzo',
    3: 'terzo',
    4: 'quarto',
    5: 'quinto',
    6: 'sesto',
    7: 'settimo',
    8: 'ottavo',
    9: 'nono',
    10: 'decimo',
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
        elif ones == 1 or ones == 8:
            return _tens[tens][:-1] + _ones[ones]
        else:
            return _tens[tens] + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds] 
        else:
            return _hundreds[hundreds] + " " + convert_less_than_hundred(less_than_hundred)

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
        return convert(numerator) + " " + _fractions[denominator] + "i"

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} e {fraction_words}"

    if number == 0:
        return "zero"

    if number < 0:
        return "meno " + convert(-number)

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