_ones= ["", "ek", "be", "tran", "char", "panch", "chha", "sat", "aath", "nav"]
_teens = ["das", "agiaar", "baar", "ter", "chaud", "pandhar", "sol", "sattar", "athaar", "ognis"]  
_tens = ["", "", "vees", "tris", "chaalis", "pachaas", "saath", "sattar", "assi", "navvu"]
_scales = [
    ["", "", ""],
    ["hazaar", "hazaar", ""],
    ["laakh", "laakh", ""],
    ["karod", "karod", ""],
    ["arab", "arab", ""],
    ["kharab", "kharab", ""],
    ["neel", "neel", ""],
    ["padma", "padma", ""],
    ["shankh", "shankh", ""]
]

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    else:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + " " + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _ones[hundreds] + "so"
        else:
            return _ones[hundreds] + "so " + convert_less_than_hundred(less_than_hundred)

def convert(number):
    if number == 0:
        return "shuunya"

    if number < 0:
        return "rin " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if scale_index > 0:
                part += " " + _scales[scale_index][1]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))