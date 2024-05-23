_ones= ["", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
_teens = ["zehn", "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]  
_tens = ["", "", "zwanzig", "dreißig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
_hundreds = ["", "einhundert", "zweihundert", "dreihundert", "vierhundert", "fünfhundert", 
             "sechshundert", "siebenhundert", "achthundert", "neunhundert"]

_scales = [
    ("", "", ""),
    ("tausend", "tausend", "tausend"),
    ("Million", "Millionen", "Millionen"),
    ("Milliarde", "Milliarden", "Milliarden"),
    ("Billion", "Billionen", "Billionen"),
    ("Billiarde", "Billiarden", "Billiarden"),
    ("Trillion", "Trillionen", "Trillionen"),
    ("Trilliarde", "Trilliarden", "Trilliarden"),
    ("Quadrillion", "Quadrillionen", "Quadrillionen"),
    ("Quadrilliarde", "Quadrilliarden", "Quadrilliarden"),
    ("Quintillion", "Quintillionen", "Quintillionen"),
    ("Quintilliarde", "Quintilliarden", "Quintilliarden"),
]

_fractions = {
    2: 'halb',
    3: 'drittel',
    4: 'viertel', 
    5: 'fünftel',
    6: 'sechstel',
    7: 'siebtel',
    8: 'achtel',
    9: 'neuntel',
    10: 'zehntel',
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
        elif tens == 1:
            return _ones[ones] + "und" + _tens[tens]
        else:
            return _ones[ones] + "und" + _tens[tens]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif number < 1000000:
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

        return f"{integer_words} Komma {fraction_words}"

    if number == 0:
        return "null"

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