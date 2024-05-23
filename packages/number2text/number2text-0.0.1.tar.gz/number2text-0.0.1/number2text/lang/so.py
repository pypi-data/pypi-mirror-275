_ones = ['', 'kow', 'labo', 'saddex', 'afar', 'shan', 'lix', 'toddoba', 'siddeed', 'sagaal']
_teens = ['toban', 'kow iyo toban', 'labo iyo toban', 'saddex iyo toban', 'afar iyo toban', 'shan iyo toban', 'lix iyo toban', 'toddoba iyo toban', 'siddeed iyo toban', 'sagaal iyo toban']
_tens = ['', '', 'labaatan', 'soddon', 'afartan', 'konton', 'lixdan', 'toddobaatan', 'siddeetan', 'sagaashan']
_scale = ['', 'boqol', 'kun', 'milyan', 'bilyan', 'tirilyan', 'kuwadirilyan', 'kuwintirilyan', 'sekstirilyan', 'septirilyan', 'oktirilyan', 'nonirilyan', 'desirilyan']

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
            return _tens[tens] + ' iyo ' + _ones[ones]
    else:
        hundreds, remainder = divmod(number, 100)
        if remainder == 0:
            return _ones[hundreds] + ' boqol'
        else:
            return _ones[hundreds] + ' boqol ' + _convert_three_digits(remainder)

def convert(number):
    if number == 0:
        return 'sifir'
    elif number < 0:
        return 'ka yar ' + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = _convert_three_digits(number % 1000)
            if scale_index > 0:
                part += ' ' + _scale[scale_index]
            parts.append(part)
        number //= 1000
        scale_index += 1

    return ' iyo '.join(reversed(parts))