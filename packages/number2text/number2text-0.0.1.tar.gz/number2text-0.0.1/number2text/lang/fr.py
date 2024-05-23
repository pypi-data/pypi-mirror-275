_ones= ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"]
_teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"]
_tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante-dix", "quatre-vingt", "quatre-vingt-dix"]
_scales = ["", "mille", "million", "milliard", "billion", "billiard", "trillion", "trilliard", "quadrillion", "quadrilliard", "quintillion", "quintilliard"]

_fractions = {
    2: 'demi',
    3: 'tiers',
    4: 'quart',
    5: 'cinquième',
    6: 'sixième',
    7: 'septième', 
    8: 'huitième',
    9: 'neuvième',
    10: 'dixième',
}

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 60:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        elif tens == 7 or tens == 9:
            return _tens[tens-1] + "-" + _teens[ones]
        else:
            return _tens[tens] + "-" + _ones[ones]
    elif number < 80:
        if number == 60:
            return "soixante"
        else:
            return "soixante-" + convert_less_than_hundred(number - 60)
    else:
        if number == 80:
            return "quatre-vingts"
        else:
            return "quatre-vingt-" + convert_less_than_hundred(number - 80)

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            if hundreds == 1:
                return "cent"
            else:
                return _ones[hundreds] + " cents"
        else:
            if hundreds == 1:
                return "cent " + convert_less_than_hundred(less_than_hundred)
            else:
                return _ones[hundreds] + " cent " + convert_less_than_hundred(less_than_hundred)

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator] + ("s" if numerator > 1 else "")

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} et {fraction_words}"

    if number == 0:
        return 'zéro'

    if number < 0:
        return 'moins ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if scale_index > 0:
                if number % 1000 == 1:
                    part = _scales[scale_index]
                else:
                    part += " " + _scales[scale_index] + ("s" if number % 1000 > 1 else "")
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))