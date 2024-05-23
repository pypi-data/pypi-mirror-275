_ones= ['', 'eka', 'deka', 'tuna', 'hatara', 'paha', 'haya', 'hata', 'ata', 'namaya']
_teens = ['dahaya', 'ekolaha', 'dolos', 'telolaha', 'tudaha', 'pahalos', 'solos', 'hatalos', 'atalos', 'ekunvissa']
_tens = ['', '', 'vissa', 'tis', 'hathalis', 'panas', 'heta', 'hattea', 'asiya', 'anuva']
_hundreds = ['', 'siyaya', 'desiya', 'tunsiya', 'harsiya', 'pansiya', 'haysiya', 'hatsiya', 'atsiya', 'namsiya']

_powers_of_ten = [
    ('dahasa', 'dahasa', 'dahasa'), 
    ('lakshaya', 'lakshaya', 'lakshaya'),
    ('koti', 'koti', 'koti'),
    ('shankaya', 'shankaya', 'shankaya'),
    ('niyutaya', 'niyutaya', 'niyutaya'),
    ('maha koti', 'maha koti', 'maha koti'),
]

_fractions = {
    2: 'ardha',
    3: 'tun baga eka',
    4: 'kala',
    5: 'pas baga eka',
    6: 'saya baga eka',
    7: 'hat baga eka',
    8: 'ata baga eka',
    9: 'nam baga eka',
    10: 'dahaya baga eka',
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
            return _tens[tens] + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + convert_less_than_thousand(less_than_hundred)

def get_power(number, power_index):
    if number == 1:
        return _powers_of_ten[power_index][0]
    elif number == 2:
        return _powers_of_ten[power_index][1]  
    else:
        return _powers_of_ten[power_index][2]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + ' ' + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)
        
        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)
        
        return f"{integer_words} dasha ansaya {fraction_words}"
    
    if number == 0:
        return 'shunya'
    
    if number < 0:
        return 'rin ' + convert(-number)
    
    parts = []
    power_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            power = get_power(number % 1000, power_index)
            if power:
                part += ' ' + power
            parts.append(part)
        number //= 1000
        power_index += 1
        
    return ' '.join(reversed(parts))