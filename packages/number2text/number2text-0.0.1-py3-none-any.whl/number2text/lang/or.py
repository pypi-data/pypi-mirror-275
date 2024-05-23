_ones= ['', 'eka', 'bā', 'tīni', 'cāri', 'pāñca', 'cha', 'sāta', 'āṭha', 'nava']
_teens = ['dasa', 'ekādasa', 'bārasa', 'terasa', 'caudasa', 'pannarasa', 'sorasa', 'satarasa', 'aṭhārasa', 'ekunīsa']
_tens = ['', '', 'bīsa', 'tirisa', 'cālīsa', 'pacāsa', 'sāṭhie', 'sattari', 'asī', 'navē']
_hundreds = ['', 'eka saẏa', 'dui saẏa', 'tini saẏa', 'cāri saẏa', 'pāñca saẏa', 'cha saẏa', 'sāta saẏa', 'āṭha saẏa', 'nava saẏa']

_powers_of_ten = [
    ('hazāra', 'hazāra', 'hazāra'),
    ('lākha', 'lākha', 'lākha'), 
    ('koṭi', 'koṭi', 'koṭi'),
    ('arab', 'arab', 'arab'),
    ('kharba', 'kharba', 'kharba'),
    ('nīla', 'nīla', 'nīla'),
    ('padma', 'padma', 'padma'),
    ('śaṅkha', 'śaṅkha', 'śaṅkha'),
    ('mahāśaṅkha', 'mahāśaṅkha', 'mahāśaṅkha'),
    ('ananta', 'ananta', 'ananta'),
]

_fractions = {
    2: 'adhā',
    3: 'eka tṛtīẏāṃśa',
    4: 'eka caturthāṃśa',
    5: 'eka pañcamāṃśa',
    6: 'eka ṣaṣṭhāṃśa',
    7: 'eka saptamāṃśa',
    8: 'eka aṣṭamāṃśa',
    9: 'eka navamāṃśa',
    10: 'eka daśamāṃśa',
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
        
        return f"{integer_words} daśamika {fraction_words}"
    
    if number == 0:
        return 'śūnya'
    
    if number < 0:
        return 'ṛṇa ' + convert(-number)
    
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