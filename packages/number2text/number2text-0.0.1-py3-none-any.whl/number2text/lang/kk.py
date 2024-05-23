_ones= ['', 'bir', 'eki', 'üş', 'tört', 'bes', 'altı', 'jeti', 'segiz', 'toğız']
_teens = ['on', 'on bir', 'on eki', 'on üş', 'on tört', 'on bes', 'on altı', 'on jeti', 'on segiz', 'on toğız']
_tens = ['', '', 'jiyırma', 'otız', 'qırıq', 'elu', 'alpıs', 'jetpis', 'seksen', 'toqsan']
_hundreds = ['', 'jüz', 'eki jüz', 'üş jüz', 'tört jüz', 'bes jüz', 'altı jüz', 'jeti jüz', 'segiz jüz', 'toğız jüz']

_powers_of_ten = [
    ('mıñ', 'mıñ', 'mıñ'), 
    ('million', 'million', 'million'),
    ('milliard', 'milliard', 'milliard'),
    ('trillion', 'trillion', 'trillion'),
    ('kvadrillion', 'kvadrillion', 'kvadrillion'),
    ('kvintillion', 'kvintillion', 'kvintillion'),
]

_fractions = {
    2: 'jarım',
    3: 'üşten bir',
    4: 'tört bölik',
    5: 'besten bir',
    6: 'altıdan bir',
    7: 'jetiden bir',
    8: 'segizden bir',
    9: 'toğızdan bir',
    10: 'onnan bir',
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
            return _tens[tens] + ' ' + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' ' + convert_less_than_thousand(less_than_hundred)

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
        
        return f"{integer_words} bütin {fraction_words}"
    
    if number == 0:
        return 'nöl'
    
    if number < 0:
        return 'mïnus ' + convert(-number)
    
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