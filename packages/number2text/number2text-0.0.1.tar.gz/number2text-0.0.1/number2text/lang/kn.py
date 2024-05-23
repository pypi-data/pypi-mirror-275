_ones= ["", "ondu", "eradu", "mooru", "naalku", "aidu", "aaru", "elu", "entu", "ombattu"]
_teens = ["hattu", "hannondu", "hanneradu", "hannooru", "hannaalu", "hannaidu", "hannaaru", "hannelu", "hannentu", "hattombattu"]
_tens = ["", "", "ippatu", "muvatu", "naalvatu", "aivatu", "aravatu", "eppattu", "embattu", "tombattu"]
_hundreds = ["", "nooru", "innooru", "moonooru", "naanooru", "ainooru", "aarooru", "elunooru", "ennooru", "ombinooru"]

_scales = [
    ("", "", ""),
    ("saavira", "saavira", "saavira"),
    ("laksha", "laksha", "laksha"),
    ("koti", "koti", "koti"),
    ("shankha", "shankha", "shankha"),
    ("padma", "padma", "padma"),
    ("nyarbudha", "nyarbudha", "nyarbudha"),
    ("parardha", "parardha", "parardha"),
    ("anta", "anta", "anta"),
    ("madhya", "madhya", "madhya"),
    ("paraardha", "paraardha", "paraardha"),
    ("maha-parardha", "maha-parardha", "maha-parardha"),
]

_fractions = {
    2: 'ardha',
    3: 'trithiya',
    4: 'chaturtha',
    5: 'panchama',
    6: 'shashta',
    7: 'saptama',
    8: 'ashtama',
    9: 'navama',
    10: 'dashama',
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

        return f"{integer_words} bhindu {fraction_words}"

    if number == 0:
        return "sonne"

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