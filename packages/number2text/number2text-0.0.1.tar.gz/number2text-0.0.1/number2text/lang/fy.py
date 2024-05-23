_ones= ["", "ien", "twa", "trije", "fjouwer", "fiif", "seis", "sân", "acht", "njoggen"]
_teens = ["tsien", "alve", "tolve", "trettjin", "fjirtjin", "fyftjin", "sechtjin", "santjin", "achttjin", "njoggentjin"]
_tens = ["", "", "tweintich", "tritich", "fjirtich", "fyftich", "sechstich", "santich", "tachtich", "njoggentich"]
_hundreds = ["", "hûndert", "twahûndert", "trijehûndert", "fjouwerhûndert", "fiifhûndert", "seishûndert", "sânhûndert", "achthûndert", "njoggenhûndert"]

_scales = [
    ("", "", ""),
    ("tûzen", "tûzen", "tûzen"),
    ("miljoen", "miljoen", "miljoen"),
    ("miljard", "miljard", "miljard"),
    ("biljoen", "biljoen", "biljoen"),
    ("biljard", "biljard", "biljard"),
    ("triljoen", "triljoen", "triljoen"),
    ("triljard", "triljard", "triljard"),
    ("kwadriljoen", "kwadriljoen", "kwadriljoen"),
    ("kwadriljard", "kwadriljard", "kwadriljard"),
]

_fractions = {
    2: 'heal',
    3: 'tredde',
    4: 'fjirde',
    5: 'fyfde',
    6: 'sechsde',
    7: 'sânde',
    8: 'achtste',
    9: 'njoggende',
    10: 'tsiende',
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
        
        return f"{integer_words} komma {fraction_words}"
    
    if number == 0:
        return "nul"
    
    if number < 0:
        return "min " + convert(-number)
    
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