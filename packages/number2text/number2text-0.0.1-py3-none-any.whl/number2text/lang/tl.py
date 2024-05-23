_ones= ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
_tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
_hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

_scales = [
    ("", "", ""),
    ("thousand", "thousand", "thousand"),
    ("million", "million", "million"),
    ("billion", "billion", "billion"),
    ("trillion", "trillion", "trillion"),
    ("quadrillion", "quadrillion", "quadrillion"),
    ("quintillion", "quintillion", "quintillion"),
    ("sextillion", "sextillion", "sextillion"),
    ("septillion", "septillion", "septillion"),
    ("octillion", "octillion", "octillion"),
    ("nonillion", "nonillion", "nonillion"),
    ("decillion", "decillion", "decillion"),
]

_fractions = {
    2: "half",
    3: "third", 
    4: "quarter",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
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
            return _tens[tens] + "-" + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    else:
        return " " + _scales[scale_index][0] 

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator] + "s"

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)
        
        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)
        
        return f"{integer_words} and {fraction_words}"
    
    if number == 0:
        return "zero"

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