_ones= ["", "jedan", "dva", "tri", "četiri", "pet", "šest", "sedam", "osam", "devet"]
_teens = ["deset", "jedanaest", "dvanaest", "trinaest", "četrnaest", "petnaest", "šesnaest", "sedamnaest", "osamnaest", "devetnaest"]
_tens = ["", "", "dvadeset", "trideset", "četrdeset", "pedeset", "šezdeset", "sedamdeset", "osamdeset", "devedeset"]
_hundreds = ["", "sto", "dvesta", "trista", "četristo", "petsto", "šesto", "sedamsto", "osamsto", "devetsto"]

_scales = [
    ("", "", ""),
    ("hiljada", "hiljade", "hiljada"),
    ("milion", "miliona", "miliona"),
    ("milijarda", "milijarde", "milijardi"),
    ("bilion", "biliona", "biliona"),
    ("bilijarda", "bilijarde", "bilijardi"),
    ("trilion", "triliona", "triliona"),
    ("trilijarda", "trilijarde", "trilijardi"),
    ("kvadrilion", "kvadriliona", "kvadriliona"),
    ("kvadrilijarda", "kvadrilijarde", "kvadrilijardi"),
    ("kvintilion", "kvintiliona", "kvintiliona"),
    ("kvintilijarda", "kvintilijarde", "kvintilijardi"),
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
        return " " + _scales[scale_index][0]
    elif 1 < number < 5:
        return " " + _scales[scale_index][1]
    else:
        return " " + _scales[scale_index][2]

def convert(number):
    if number == 0:
        return "nula"

    if number < 0:
        return "minus " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            parts.append(part + scale)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))