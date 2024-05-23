_ones= ["", "ఒకటి", "రెండు", "మూడు", "నాలుగు", "ఐదు", "ఆరు", "ఏడు", "ఎనిమిది", "తొమ్మిది"]
_teens = ["పది", "పదకొండు", "పన్నెండు", "పదమూడు", "పద్నాలుగు", "పదిహేను", "పదహారు", "పదిహేడు", "పద్దెనిమిది", "పంతొమ్మిది"] 
_tens = ["", "", "ఇరవై", "ముప్పై", "నలభై", "యాభై", "అరవై", "డెబ్బై", "ఎనభై", "తొంభై"]
_hundreds = ["", "వంద", "రెండు వందలు", "మూడు వందలు", "నాలుగు వందలు", "ఐదు వందలు", "ఆరు వందలు", "ఏడు వందలు", "ఎనిమిది వందలు", "తొమ్మిది వందలు"]

_scales = [
    ("", "", ""),
    ("వేయి", "వేలు", "వేల"),
    ("లక్ష", "లక్షలు", "లక్షల"),
    ("కోటి", "కోట్లు", "కోట్ల"),
    ("వంద కోట్లు", "వంద కోట్లు", "వంద కోట్ల"),
    ("వేయి కోట్లు", "వేయి కోట్లు", "వేయి కోట్ల"),
    ("లక్ష కోట్లు", "లక్ష కోట్లు", "లక్ష కోట్ల"),
    ("కోటి కోట్లు", "కోటి కోట్లు", "కోటి కోట్ల"),
    ("వంద కోటి కోట్లు", "వంద కోటి కోట్లు", "వంద కోటి కోట్ల"),
    ("వేయి కోటి కోట్లు", "వేయి కోటి కోట్లు", "వేయి కోటి కోట్ల"),
    ("లక్ష కోటి కోట్లు", "లక్ష కోటి కోట్లు", "లక్ష కోటి కోట్ల"),
]

_fractions = {
    2: 'సగం',
    3: 'మూడింట ఒక వంతు', 
    4: 'పావు',
    5: 'ఐదింట ఒక వంతు',
    6: 'ఆరింట ఒక వంతు',
    7: 'ఏడింట ఒక వంతు',
    8: 'ఎనిమిదింట ఒక వంతు',
    9: 'తొమ్మిదింట ఒక వంతు',
    10: 'పదింట ఒక వంతు',
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
    elif number > 1 and number <= 10:
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

        return f"{integer_words} దశాంశం {fraction_words}"

    if number == 0:
        return "సున్నా"

    if number < 0:
        return "ఋణాత్మక " + convert(-number)

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