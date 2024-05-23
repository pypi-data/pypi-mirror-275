_ones= ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
_teens = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
_tens = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
_hundreds = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

_scales = [
    ("", "", ""),
    ("mil", "mil", "mil"),
    ("milhão", "milhões", "milhões"),
    ("bilhão", "bilhões", "bilhões"),
    ("trilhão", "trilhões", "trilhões"),
    ("quatrilhão", "quatrilhões", "quatrilhões"),
    ("quintilhão", "quintilhões", "quintilhões"),
    ("sextilhão", "sextilhões", "sextilhões"),
    ("septilhão", "septilhões", "septilhões"),
    ("octilhão", "octilhões", "octilhões"),
    ("nonilhão", "nonilhões", "nonilhões"),
    ("decilhão", "decilhões", "decilhões"),
]

_fractions = {
    2: 'meio',
    3: 'terço',
    4: 'quarto',
    5: 'quinto',
    6: 'sexto',
    7: 'sétimo',
    8: 'oitavo',
    9: 'nono',
    10: 'décimo',
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
        return convert(numerator) + " " + _fractions[denominator] + ("s" if numerator > 1 else "")

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} vírgula {fraction_words}"

    if number == 0:
        return "zero"

    if number < 0:
        return "menos " + convert(-number)

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