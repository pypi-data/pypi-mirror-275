_ones= ['', 'vienas', 'du', 'trys', 'keturi', 'penki', 'šeši', 'septyni', 'aštuoni', 'devyni']
_teens = ['dešimt', 'vienuolika', 'dvylika', 'trylika', 'keturiolika', 'penkiolika', 'šešiolika', 'septyniolika', 'aštuoniolika', 'devyniolika']
_tens = ['', '', 'dvidešimt', 'trisdešimt', 'keturiasdešimt', 'penkiasdešimt', 'šešiasdešimt', 'septyniasdešimt', 'aštuoniasdešimt', 'devyniasdešimt']
_hundreds = ['', 'šimtas', 'du šimtai', 'trys šimtai', 'keturi šimtai', 'penki šimtai', 'šeši šimtai', 'septyni šimtai', 'aštuoni šimtai', 'devyni šimtai']

_powers_of_ten = [
    ('tūkstantis', 'tūkstančių'), 
    ('milijonas', 'milijonų'),
    ('milijardas', 'milijardų'),
    ('trilijonas', 'trilijonų'),
    ('kvadrilijonas', 'kvadrilijonų'),
    ('kvintilijonas', 'kvintilijonų')
]

_fractions = {
    2: 'pusė',
    3: 'trečdalis', 
    4: 'ketvirtadalis',
    5: 'penktadalis',
    6: 'šeštadalis',
    7: 'septintadalis',
    8: 'aštuntadalis',
    9: 'devintadalis',
    10: 'dešimtadalis'
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
    if power_index == 0:
        if 10 < number < 20 or number % 10 == 0:
            return _powers_of_ten[power_index][1]
        else:
            return _powers_of_ten[power_index][0]
    else:
        return _powers_of_ten[power_index][1]

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

        return f"{integer_words} ir {fraction_words}"

    if number == 0:
        return 'nulis'

    if number < 0:
        return 'minus ' + convert(-number)

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