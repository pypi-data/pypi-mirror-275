_ones= ["", "eka", "dua", "tria", "patra", "penta", "hexa", "hepta", "okta", "nona"]
_teens = ["deka", "deka eka", "deka dua", "deka tria", "deka patra", "deka penta", "deka hexa", "deka hepta", "deka okta", "deka nona"]
_tens = ["", "", "duadeka", "triadeka", "patradeka", "pentadeka", "hexadeka", "heptadeka", "oktadeka", "nonadeka"] 
_hundreds = ["", "hekto", "dihekto", "trihekto", "tetrahekto", "pentahekto", "hexahekto", "heptahekto", "oktahekto", "nonahekto"]

_scales = [
    ("", "", ""),
    ("kilo", "kilo", "kilo"),
    ("mega", "mega", "mega"),
    ("giga", "giga", "giga"),
    ("tera", "tera", "tera"),
    ("peta", "peta", "peta"),
    ("exa", "exa", "exa"),
    ("zetta", "zetta", "zetta"),
    ("yotta", "yotta", "yotta"),
]

_fractions = {
    2: 'hemi',
    3: 'triti', 
    4: 'tetarti',
    5: 'pempti',
    6: 'hekti',
    7: 'hebdomi',
    8: 'ogdoi',
    9: 'enati',
    10: 'dekati'
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
        
        return f"{integer_words} koma {fraction_words}"
    
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
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1
    
    return " ".join(reversed(parts))