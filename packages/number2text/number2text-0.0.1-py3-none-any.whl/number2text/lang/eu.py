_ones= ['', 'bat', 'bi', 'hiru', 'lau', 'bost', 'sei', 'zazpi', 'zortzi', 'bederatzi']
_teens = ['hamar', 'hamaika', 'hamabi', 'hamahiru', 'hamalau', 'hamabost', 'hamasei', 'hamazazpi', 'hemezortzi', 'hemeretzi'] 
_tens = ['', '', 'hogei', 'hogeita hamar', 'berrogei', 'berrogeita hamar', 'hirurogei', 'hirurogeita hamar', 'laurogei', 'laurogeita hamar']
_hundreds = ['', 'ehun', 'berrehun', 'hirurehun', 'laurehun', 'bostehun', 'seiehun', 'zazpiehun', 'zortziehun', 'bederatziehun']

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number-10]
    else:
        tens, ones = divmod(number, 10)
        if ones > 0:
            return _tens[tens] + ' eta ' + _ones[ones]
        else:
            return _tens[tens]

def convert_less_than_thousand(number):
    hundreds, less_than_hundred = divmod(number, 100)
    if hundreds == 0:
        return convert_less_than_hundred(less_than_hundred)
    elif less_than_hundred == 0:
        return _hundreds[hundreds]
    else:
        return _hundreds[hundreds] + ' eta ' + convert_less_than_hundred(less_than_hundred)

def convert(number):
    if number == 0:
        return 'zero'

    if number < 0:
        return 'minus ' + convert(-number)

    parts = []
    
    if number >= 1000000000:
        billions, number = divmod(number, 1000000000)
        parts.append(convert_less_than_thousand(billions) + ' mila milioi')

    if number >= 1000000:
        millions, number = divmod(number, 1000000)
        parts.append(convert_less_than_thousand(millions) + ' milioi')
        
    if number >= 1000:
        thousands, number = divmod(number, 1000)
        parts.append(convert_less_than_thousand(thousands) + ' mila')

    if number > 0:
        parts.append(convert_less_than_thousand(number))

    return ' '.join(parts)