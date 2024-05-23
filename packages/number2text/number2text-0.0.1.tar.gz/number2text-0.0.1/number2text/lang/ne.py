_ones= ["", "एक", "दुई", "तीन", "चार", "पाँच", "छ", "सात", "आठ", "नौ"]
_teens = ["दस", "एघार", "बाह्र", "तेह्र", "चौध", "पन्ध्र", "सोह्र", "सत्र", "अठार", "उन्नाइस"]
_tens = ["", "", "बीस", "तीस", "चालीस", "पचास", "साठी", "सत्तरी", "अस्सी", "नब्बे"]
_scales = ["", "हजार", "लाख", "करोड", "अर्ब", "खर्ब", "नील", "पद्म", "शंख"]

_fractions = {
    2: 'आधा',
    3: 'एक तिहाई',
    4: 'एक चौथाई', 
    5: 'एक पाँचवाँ',
    6: 'एक छैठाँ',
    7: 'एक सातौं',
    8: 'एक आठौं',
    9: 'एक नवौं',
    10: 'एक दसौं',
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
        else:
            return _tens[tens] + " " + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _ones[hundreds] + " सय"
        else:
            return _ones[hundreds] + " सय " + convert_less_than_hundred(less_than_hundred)

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

        return f"{integer_words} दशमलव {fraction_words}"

    if number == 0:
        return "शून्य"

    if number < 0:
        return "ऋणात्मक " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if scale_index > 0:
                part += " " + _scales[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))