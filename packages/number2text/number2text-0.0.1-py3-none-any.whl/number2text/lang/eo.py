_ones= ["", "unu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "naŭ"]
_teens = ["dek", "dek unu", "dek du", "dek tri", "dek kvar", "dek kvin", "dek ses", "dek sep", "dek ok", "dek naŭ"]
_tens = ["", "", "dudek", "tridek", "kvardek", "kvindek", "sesdek", "sepdek", "okdek", "naŭdek"]
_hundreds = ["", "cent", "ducent", "tricent", "kvarcent", "kvincent", "sescent", "sepcent", "okcent", "naŭcent"]

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

def convert(number):
    if number == 0:
        return "nulo"

    if number < 0:
        return "minus " + convert(-number)

    parts = []
    scale = 1000000000000
    scale_names = ["", "mil", "milionoj", "miliardoj", "bilionoj", "biliardoj", "trilionoj", "triliardoj"]

    while scale > 0:
        if number >= scale:
            part = convert_less_than_thousand(number // scale)
            if scale > 1:
                part += " " + scale_names[len(str(scale)) // 3]
            parts.append(part)
            number %= scale
        scale //= 1000

    if number > 0:
        parts.append(convert_less_than_thousand(number))

    return " ".join(parts)