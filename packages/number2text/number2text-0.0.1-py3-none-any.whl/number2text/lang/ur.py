_ones= ["", "ek", "do", "teen", "chaar", "paanch", "chhe", "saat", "aath", "nau"]
_teens = ["das", "gyaarah", "baarah", "terah", "chaudah", "pandrah", "solah", "satrah", "athaarah", "unnis"]  
_tens = ["", "", "bees", "tees", "chaalis", "pachaas", "saath", "sattar", "assi", "navve"]
_hundreds = ["", "ek sau", "do sau", "teen sau", "chaar sau", "paanch sau", "chhe sau", "saat sau", "aath sau", "nau sau"]

_scales = [
    ("", "", ""),
    ("hazaar", "hazaar", "hazaar"),
    ("laakh", "laakh", "laakh"), 
    ("karod", "karod", "karod"),
    ("arab", "arab", "arab"),
    ("kharab", "kharab", "kharab"),
    ("neel", "neel", "neel"),
    ("padma", "padma", "padma"),
    ("shankh", "shankh", "shankh"),
    ("mahashankh", "mahashankh", "mahashankh"),
    ("ank", "ank", "ank"),
    ("jald", "jald", "jald"),
]

_fractions = {
    2: 'aadha',
    3: 'ek tihaaee',
    4: 'ek chauthaee', 
    5: 'ek panchmaa',
    6: 'ek chhataa',
    7: 'ek saatmaa',
    8: 'ek aathmaa',
    9: 'ek nauvaa',
    10: 'ek dasmaa',
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

        return f"{integer_words} dushmalaa {fraction_words}"

    if number == 0:
        return "sifar"

    if number < 0:
        return "manfi " + convert(-number)

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