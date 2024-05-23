_ones= ["", "ཞིག་", "གཉིས་", "གསུམ་", "བཞི་", "ལྔ་", "དྲུག་", "བདུན་", "བརྒྱད་", "དགུ་"]
_tens = ["", "བཅུ་", "ཉི་ཤུ་", "སུམ་ཅུ་", "བཞི་བཅུ་", "ལྔ་བཅུ་", "དྲུག་ཅུ་", "བདུན་ཅུ་", "བརྒྱད་ཅུ་", "དགུ་བཅུ་"]
_hundreds = ["", "བརྒྱ་", "ཉིས་བརྒྱ་", "སུམ་བརྒྱ་", "བཞི་བརྒྱ་", "ལྔ་བརྒྱ་", "དྲུག་བརྒྱ་", "བདུན་བརྒྱ་", "བརྒྱད་བརྒྱ་", "དགུ་བརྒྱ་"]
_thousands = ["", "སྟོང་", "ཁྲི་", "འབུམ་", "ས་ཡ་", "བྱེ་བ་", "དུང་ཕྱུར་", "ས་ཡ་ཕྲག་", "བྱེ་བ་ཕྲག་", "དུང་ཕྱུར་ཕྲག་"]

def convert_less_than_thousand(number):
    if number < 10:
        return _ones[number]
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

def convert(number):
    if number == 0:
        return "ཀླད་ཀོར་"

    if number < 0:
        return "ཉུང་ཤོས་" + convert(-number)

    parts = []
    thousand_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            if thousand_index > 0:
                part += _thousands[thousand_index]
            parts.append(part)
        number //= 1000
        thousand_index += 1

    return "".join(reversed(parts))