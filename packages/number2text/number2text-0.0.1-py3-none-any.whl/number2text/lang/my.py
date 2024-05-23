_ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
_teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'] 
_tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
_hundreds = ['', 'one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred']

_scales = [
    ('', '', ''),
    ('thousand', 'thousand', 'thousand'),
    ('million', 'million', 'million'), 
    ('billion', 'billion', 'billion'),
    ('trillion', 'trillion', 'trillion'),
    ('quadrillion', 'quadrillion', 'quadrillion'),
    ('quintillion', 'quintillion', 'quintillion'),
    ('sextillion', 'sextillion', 'sextillion'),
    ('septillion', 'septillion', 'septillion'),
    ('octillion', 'octillion', 'octillion'),
    ('nonillion', 'nonillion', 'nonillion'),
    ('decillion', 'decillion', 'decillion'),
    ('undecillion', 'undecillion', 'undecillion'), 
    ('duodecillion', 'duodecillion', 'duodecillion'),
    ('tredecillion', 'tredecillion', 'tredecillion'),
    ('quattuordecillion', 'quattuordecillion', 'quattuordecillion'),
    ('quindecillion', 'quindecillion', 'quindecillion'),
    ('sexdecillion', 'sexdecillion', 'sexdecillion')
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
            return _tens[tens] + '-' + _ones[ones]

def convert_less_than_thousand(number):
    if number < 100:
        return convert_less_than_hundred(number)
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds] 
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_hundred(less_than_hundred)
        
def convert(number):
    if number == 0:
        return 'zero'

    if number < 0:
        return 'negative ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = _scales[scale_index][0]
            if scale_index > 0:
                part = part + ' ' + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))