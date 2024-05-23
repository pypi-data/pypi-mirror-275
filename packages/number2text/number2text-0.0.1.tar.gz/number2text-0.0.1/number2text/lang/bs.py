_ones= ["", "ek", "dui", "tin", "char", "pach", "choy", "sat", "at", "noy"]
_teens = ["dosh", "egaro", "baro", "tero", "chuddho", "ponero", "sholo", "sotero", "athero", "unish"]
_tens = ["", "", "bish", "trish", "cholish", "ponchas", "chollish", "shattor", "ashi", "nobboi"]
_hundreds = ["", "ek sho", "dui sho", "tin sho", "char sho", "pach sho", "choy sho", "sat sho", "at sho", "noy sho"]

_scales = [
    ("", "", ""),
    ("hajar", "hajar", "hajar"),
    ("lakh", "lakh", "lakh"),
    ("koti", "koti", "koti"),
    ("shonkha", "shonkha", "shonkha"),
    ("podmo", "podmo", "podmo"),
    ("neel", "neel", "neel"),
    ("moha neel", "moha neel", "moha neel"),
    ("shishu", "shishu", "shishu"),
    ("singho", "singho", "singho"),
    ("moha singho", "moha singho", "moha singho"),
    ("ongko", "ongko", "ongko"),
]

_fractions = {
    2: 'half',
    3: 'trutio',
    4: 'chaturthash',
    5: 'ponchomash',
    6: 'shasthash',
    7: 'saptamash',
    8: 'ashtamash',
    9: 'nobomash',
    10: 'doshomash',
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

        return f"{integer_words} doshomik {fraction_words}"

    if number == 0:
        return "shunno"

    if number < 0:
        return "rina " + convert(-number)

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