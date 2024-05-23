_ones= ["", "ɗaya", "biyu", "uku", "huɗu", "biyar", "shida", "bakwai", "takwas", "tara"]
_teens = ["goma", "goma sha ɗaya", "goma sha biyu", "goma sha uku", "goma sha huɗu", "goma sha biyar", "goma sha shida", "goma sha bakwai", "goma sha takwas", "goma sha tara"]
_tens = ["", "", "ashirin", "talatin", "arba'in", "hamsin", "sittin", "saba'in", "tamanin", "tis'in"]
_hundreds = ["", "ɗari", "ɗari biyu", "ɗari uku", "ɗari huɗu", "ɗari biyar", "ɗari shida", "ɗari bakwai", "ɗari takwas", "ɗari tara"]

_scales = [
    ("", "", ""),
    ("dubu", "dubu", "dubu"),
    ("miliyan", "miliyan", "miliyan"),
    ("biliyan", "biliyan", "biliyan"),
    ("triliyan", "triliyan", "triliyan"),
    ("kwadiriliyan", "kwadiriliyan", "kwadiriliyan"),
    ("kwintiliyan", "kwintiliyan", "kwintiliyan"),
    ("sikstiliyan", "sikstiliyan", "sikstiliyan"),
    ("siptiliyan", "siptiliyan", "siptiliyan"),
    ("oktiliyan", "oktiliyan", "oktiliyan"),
    ("noniliyan", "noniliyan", "noniliyan"),
    ("disiliyan", "disiliyan", "disiliyan"),
]

_fractions = {
    2: 'rabi',
    3: 'sulusi',
    4: 'kwata',
    5: 'humusi',
    6: 'sudusi',
    7: 'subi',
    8: 'sumuni',
    9: 'tusi',
    10: 'ushuri',
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
            return _tens[tens] + " da " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " da " + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    else:
        return _scales[scale_index][0]

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

        return f"{integer_words} da {fraction_words}"

    if number == 0:
        return "sifir"

    if number < 0:
        return "mafi " + convert(-number)

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

    return " da ".join(reversed(parts))