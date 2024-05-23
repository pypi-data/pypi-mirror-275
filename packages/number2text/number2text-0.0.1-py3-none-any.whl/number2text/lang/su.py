_ones= ["", "siji", "loro", "telu", "papat", "lima", "enem", "pitu", "wolu", "sanga"]
_teens = ["sepuluh", "sewelas", "rolas", "telulas", "patbelas", "limolas", "nembelas", "pitulas", "wolulas", "sangalas"]
_tens = ["", "", "rongpuluh", "telungpuluh", "patangpuluh", "seket", "suwidak", "pitungpuluh", "wolungpuluh", "sangang puluh"]
_hundreds = ["", "satus", "rongatus", "telungatus", "patangatus", "limangatus", "nematus", "pitungatus", "wolungatus", "sangaatus"]

_scales = [
    ("", "", ""),
    ("ewu", "ewu", "ewu"),
    ("yuta", "yuta", "yuta"),
    ("milyar", "milyar", "milyar"),
    ("trilyun", "trilyun", "trilyun"),
    ("kuadriliun", "kuadriliun", "kuadriliun"),
    ("kuintiliun", "kuintiliun", "kuintiliun"),
    ("sekstiliun", "sekstiliun", "sekstiliun"),
    ("septiliun", "septiliun", "septiliun"),
    ("oktiliun", "oktiliun", "oktiliun"),
    ("noniliun", "noniliun", "noniliun"),
    ("desiliun", "desiliun", "desiliun"),
]

_fractions = {
    2: 'setengah',
    3: 'sepertelu',
    4: 'seperempat',
    5: 'seperlima',
    6: 'seperenem',
    7: 'seperpitu',
    8: 'seperwolu',
    9: 'sepersanga',
    10: 'sepersepuluh',
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

        return f"{integer_words} koma {fraction_words}"

    if number == 0:
        return "nol"

    if number < 0:
        return "negatif " + convert(-number)

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