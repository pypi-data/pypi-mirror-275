_ones= ["", "꯱", "ꯈꯅꯤ", "ꯑꯍꯨꯝ", "ꯃꯔꯤ", "ꯃꯡꯈꯥ", "ꯇꯔꯨꯛ", "ꯇꯔꯦꯠ", "ꯅꯤꯄꯥꯟ", "ꯃꯄꯥꯟ"]
_tens = ["", "ꯆꯥ", "ꯀꯨꯟꯊꯕ", "ꯀꯨꯟꯊꯕꯁꯨꯝ", "ꯅꯤꯗꯨꯝ", "ꯑꯡꯈꯥ", "ꯍꯨꯡꯈꯥ", "ꯍꯨꯡꯈꯥꯗꯨꯝ", "ꯅꯤꯄꯥꯟꯗꯨꯝ", "ꯃꯄꯥꯟꯗꯨꯝ"]

def convert_less_than_hundred(number):
    if number < 10:
        return _ones[number]
    elif number < 20:
        return _ones[number % 10] + "ꯊꯣꯛꯄꯥ"
    else:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + _ones[ones]

def convert(number):
    if number == 0:
        return "ꯄꯨꯟꯗꯔꯤ"

    if number < 0:
        return "ꯑꯊꯣꯛꯄꯥ " + convert(-number)

    parts = []
    lakhs, less_than_lakh = divmod(number, 100000)
    if lakhs > 0:
        parts.append(convert(lakhs) + " ꯂꯥꯈ")
        number = less_than_lakh

    thousands, less_than_thousand = divmod(number, 1000)
    if thousands > 0:
        parts.append(convert(thousands) + " ꯆꯤꯡ")
        number = less_than_thousand

    hundreds, less_than_hundred = divmod(number, 100)
    if hundreds > 0:
        parts.append(convert_less_than_hundred(hundreds) + " ꯆꯥꯃꯥ")
        number = less_than_hundred

    if number > 0:
        parts.append(convert_less_than_hundred(number))

    return " ".join(parts)