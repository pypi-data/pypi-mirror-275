_ones= ["", "iray", "roa", "telo", "efatra", "dimy", "enina", "fito", "valo", "sivy"]
_teens = ["folo", "iraika ambin'ny folo", "roa ambin'ny folo", "telo ambin'ny folo", "efatra ambin'ny folo", "dimy ambin'ny folo", "enina ambin'ny folo", "fito ambin'ny folo", "valo ambin'ny folo", "sivy ambin'ny folo"]
_tens = ["", "", "roapolo", "telopolo", "efapolo", "dimampolo", "enimpolo", "fitopolo", "valopolo", "sivifolo"]
_hundreds = ["", "zato", "roanjato", "telonjato", "efajato", "dimanjato", "eninjato", "fitonjato", "valonjato", "sivinjato"]

_scales = [
    ("", "", ""),
    ("arivo", "arivo", "arivo"),
    ("tapitrisa", "tapitrisa", "tapitrisa"),
    ("lavitrisa", "lavitrisa", "lavitrisa"),
    ("biliona", "biliona", "biliona"),
    ("biliona zato", "biliona zato", "biliona zato"),
    ("triliona", "triliona", "triliona"),
    ("triliona zato", "triliona zato", "triliona zato"),
    ("kvadriliona", "kvadriliona", "kvadriliona"),
    ("kvadriliona zato", "kvadriliona zato", "kvadriliona zato"),
    ("kvintiliona", "kvintiliona", "kvintiliona"),
    ("kvintiliona zato", "kvintiliona zato", "kvintiliona zato"),
]

_fractions = {
    2: 'sasany',
    3: 'ampahatelony',
    4: 'ampahefany',
    5: 'ampahafolo',
    6: 'ampahafolo enina',
    7: 'ampahafolo fito',
    8: 'ampahafolo valo',
    9: 'ampahafolo sivy',
    10: 'ampahafolo',
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
            return _tens[tens] + " sy " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " sy " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} sy {fraction_words}"

    if number == 0:
        return "aotra"

    if number < 0:
        return "latsaka " + convert(-number)

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