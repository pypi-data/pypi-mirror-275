_ones = ["", "un", "dous", "tres", "catro", "cinco", "seis", "sete", "oito", "nove"]
_teens = ["dez", "once", "doce", "trece", "catorce", "quince", "dezaseis", "dezasete", "dezaoito", "dezanove"]
_tens = ["", "", "vinte", "trinta", "corenta", "cincuenta", "sesenta", "setenta", "oitenta", "noventa"]
_hundreds = ["", "cento", "duascentos", "trescentos", "catrocentos", "quiñentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

_scales = [
    ("", "", ""),
    ("mil", "mil", "mil"),
    ("millón", "millóns", "millóns"),
    ("mil millóns", "mil millóns", "mil millóns"),
    ("billón", "billóns", "billóns"),
    ("mil billóns", "mil billóns", "mil billóns"),
    ("trillón", "trillóns", "trillóns"),
    ("mil trillóns", "mil trillóns", "mil trillóns"),
    ("cuadrillón", "cuadrillóns", "cuadrillóns"),
    ("mil cuadrillóns", "mil cuadrillóns", "mil cuadrillóns"),
    ("quintillón", "quintillóns", "quintillóns"),
    ("mil quintillóns", "mil quintillóns", "mil quintillóns"),
]

def convert_less_than_thousand(number, is_feminine=False):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        elif ones == 1:
            if tens == 2:
                return "vinte e un" if not is_feminine else "vinte e unha"
            else:
                return _tens[tens] + " e un" if not is_feminine else _tens[tens] + " e unha"
        else:
            return _tens[tens] + " e " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            if hundreds == 1:
                return "cen"
            else:
                return _hundreds[hundreds]
        else:
            if hundreds == 1:
                return "cento " + convert_less_than_thousand(less_than_hundred, is_feminine)
            else:
                return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred, is_feminine)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif number < 1000000:
        return _scales[scale_index][1] 
    else:
        return _scales[scale_index][2]

def convert(number, is_feminine=False):
    if number == 0:
        return "cero"

    if number < 0:
        return "menos " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000, is_feminine and scale_index == 1)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))