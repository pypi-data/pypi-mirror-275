_ones= ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
_teens = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
_tens = ["", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]
_hundreds = ["", "seratus", "dua ratus", "tiga ratus", "empat ratus", "lima ratus", "enam ratus", "tujuh ratus", "delapan ratus", "sembilan ratus"]

_scales = [
    ("", "", ""),
    ("ribu", "ribu", "ribu"),
    ("juta", "juta", "juta"),
    ("miliar", "miliar", "miliar"),
    ("triliun", "triliun", "triliun"),
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
    3: 'sepertiga',
    4: 'seperempat',
    5: 'seperlima',
    6: 'seperenam',
    7: 'sepertujuh',
    8: 'seperdelapan',
    9: 'sepersembilan',
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
    elif number > 1:
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