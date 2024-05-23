_ones= ["", "një", "dy", "tre", "katër", "pesë", "gjashtë", "shtatë", "tetë", "nëntë"]
_teens = ["dhjetë", "njëmbëdhjetë", "dymbëdhjetë", "trembëdhjetë", "katërmbëdhjetë", "pesëmbëdhjetë", "gjashtëmbëdhjetë", "shtatëmbëdhjetë", "tetëmbëdhjetë", "nëntëmbëdhjetë"]
_tens = ["", "", "njëzet", "tridhjetë", "dyzet", "pesëdhjetë", "gjashtëdhjetë", "shtatëdhjetë", "tetëdhjetë", "nëntëdhjetë"]
_hundreds = ["", "njëqind", "dyqind", "treqind", "katërqind", "pesëqind", "gjashtëqind", "shtatëqind", "tetëqind", "nëntëqind"]

_scales = [
    ("", "", ""),
    ("mijë", "mijë", "mijë"),
    ("milion", "milionë", "milionë"),
    ("miliard", "miliardë", "miliardë"),
    ("bilion", "bilionë", "bilionë"),
    ("biliard", "biliardë", "biliardë"),
    ("trilion", "trilionë", "trilionë"),
    ("triliard", "triliardë", "triliardë"),
    ("kuadrilion", "kuadrilionë", "kuadrilionë"),
    ("kuadriliard", "kuadriliardë", "kuadriliardë"),
    ("kuintilion", "kuintilionë", "kuintilionë"),
    ("kuintiliard", "kuintiliardë", "kuintiliardë"),
]

_fractions = {
    2: 'gjysëm',
    3: 'e treta',
    4: 'e katërta',
    5: 'e pesta',
    6: 'e gjashta',
    7: 'e shtata',
    8: 'e teta',
    9: 'e nënta',
    10: 'e dhjeta',
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
            return _tens[tens] + " e " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " e " + convert_less_than_thousand(less_than_hundred)

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

        return f"{integer_words} presje {fraction_words}"

    if number == 0:
        return "zero"

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