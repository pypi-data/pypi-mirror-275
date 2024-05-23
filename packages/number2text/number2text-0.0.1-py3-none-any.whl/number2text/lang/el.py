_ones= ["", "ena", "dyo", "tria", "tessera", "pente", "exi", "efta", "okto", "ennea"]
_teens = ["deka", "enteka", "dodeka", "dekatria", "dekatessera", "dekapente", "dekaexe", "dekaefta", "dekaokto", "dekaennea"]
_tens = ["", "", "eikosi", "trianta", "saranta", "peninta", "exinta", "evdominta", "ogdonta", "eneninta"]
_hundreds = ["", "ekato", "diakosia", "triakosia", "tetrakosia", "pentakosia", "exakosia", "eftakosia", "oktakosia", "enniakosia"]

_scales = [
    ["", "", ""],
    ["chilia", "chiliades", "chiliadon"],
    ["ekatommyria", "ekatommyria", "ekatommyrion"],
    ["ekatommyrio", "ekatommyria", "ekatommyrion"],
    ["dis ekatommyrio", "dis ekatommyria", "dis ekatommyrion"],
    ["tris ekatommyrio", "tris ekatommyria", "tris ekatommyrion"],
    ["tetrakis ekatommyrio", "tetrakis ekatommyria", "tetrakis ekatommyrion"],
    ["pentakis ekatommyrio", "pentakis ekatommyria", "pentakis ekatommyrion"],
    ["exakis ekatommyrio", "exakis ekatommyria", "exakis ekatommyrion"],
    ["eptakis ekatommyrio", "eptakis ekatommyria", "eptakis ekatommyrion"],
    ["oktakis ekatommyrio", "oktakis ekatommyria", "oktakis ekatommyrion"],
    ["enneakis ekatommyrio", "enneakis ekatommyria", "enneakis ekatommyrion"],
]

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
    elif number >= 2 and number <= 4:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert(number):
    if number == 0:
        return "miden"

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