_ones= ['', 'einn', 'tveir', 'þrír', 'fjórir', 'fimm', 'sex', 'sjö', 'átta', 'níu']
_teens = ['tíu', 'ellefu', 'tólf', 'þrettán', 'fjórtán', 'fimmtán', 'sextán', 'sautján', 'átján', 'nítján']
_tens = ['', '', 'tuttugu', 'þrjátíu', 'fjörutíu', 'fimmtíu', 'sextíu', 'sjötíu', 'áttatíu', 'níutíu']
_hundreds = ['', 'eitt hundrað', 'tvö hundruð', 'þrjú hundruð', 'fjögur hundruð', 'fimm hundruð', 'sex hundruð', 'sjö hundruð', 'átta hundruð', 'níu hundruð']
_scales = ['', 'þúsund', 'milljón', 'milljarður', 'billjón', 'biljarður', 'trilljón', 'triljarður', 'kvadrilljón', 'kvadriljarður', 'kvintilljón', 'kvintiljarður']

def _convert_three_digits(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + ' og ' + _ones[ones]
    else:
        hundreds, remainder = divmod(number, 100)
        if remainder == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + ' og ' + _convert_three_digits(remainder)

def convert(number):
    if number == 0:
        return 'núll'
    elif number < 0:
        return 'mínus ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = _convert_three_digits(number % 1000)
            if scale_index > 0:
                part += ' ' + _scales[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' '.join(reversed(parts))