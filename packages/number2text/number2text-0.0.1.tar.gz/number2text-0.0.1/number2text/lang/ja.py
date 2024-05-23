_ones= ["", "一", "二", "三", "四", "五", "六", "七", "八", "九"]
_tens = ["", "十", "二十", "三十", "四十", "五十", "六十", "七十", "八十", "九十"]
_hundreds = ["", "百", "二百", "三百", "四百", "五百", "六百", "七百", "八百", "九百"]
_thousands = ["", "千", "二千", "三千", "四千", "五千", "六千", "七千", "八千", "九千"]
_ten_thousands = ["", "万", "二万", "三万", "四万", "五万", "六万", "七万", "八万", "九万"]
_hundred_millions = ["", "億", "二億", "三億", "四億", "五億", "六億", "七億", "八億", "九億"]

def convert_less_than_ten_thousand(number):
    if number < 10:
        return _ones[number]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + _ones[ones]
    elif number < 1000:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + convert_less_than_ten_thousand(less_than_hundred)
    else:
        thousands, less_than_thousand = divmod(number, 1000)
        if less_than_thousand == 0:
            return _thousands[thousands]
        else:
            return _thousands[thousands] + convert_less_than_ten_thousand(less_than_thousand)

def convert(number):
    if number == 0:
        return "零"

    if number < 0:
        return "負" + convert(-number)

    parts = []
    hundred_millions, less_than_hundred_million = divmod(number, 100000000)
    if hundred_millions > 0:
        parts.append(convert_less_than_ten_thousand(hundred_millions) + "億")
        number = less_than_hundred_million

    ten_thousands, less_than_ten_thousand = divmod(number, 10000)
    if ten_thousands > 0:
        parts.append(convert_less_than_ten_thousand(ten_thousands) + "万")
        number = less_than_ten_thousand

    if number > 0:
        parts.append(convert_less_than_ten_thousand(number))

    return "".join(parts)