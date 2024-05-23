_ones= ["", "ໜຶ່ງ", "ສອງ", "ສາມ", "ສີ່", "ຫ້າ", "ຫົກ", "ເຈັດ", "ແປດ", "ເກົ້າ"]
_teens = ["ສິບ", "ສິບເອັດ", "ສິບສອງ", "ສິບສາມ", "ສິບສີ່", "ສິບຫ້າ", "ສິບຫົກ", "ສິບເຈັດ", "ສິບແປດ", "ສິບເກົ້າ"]
_tens = ["", "", "ຊາວ", "ສາມສິບ", "ສີ່ສິບ", "ຫ້າສິບ", "ຫົກສິບ", "ເຈັດສິບ", "ແປດສິບ", "ເກົ້າສິບ"]
_hundreds = ["", "ໜຶ່ງຮ້ອຍ", "ສອງຮ້ອຍ", "ສາມຮ້ອຍ", "ສີ່ຮ້ອຍ", "ຫ້າຮ້ອຍ", "ຫົກຮ້ອຍ", "ເຈັດຮ້ອຍ", "ແປດຮ້ອຍ", "ເກົ້າຮ້ອຍ"]

_powers = [
    ("", "", ""),
    ("ພັນ", "ພັນ", "ພັນ"),
    ("ລ້ານ", "ລ້ານ", "ລ້ານ"),
    ("ຕື້", "ຕື້", "ຕື້"),
    ("ພັນຕື້", "ພັນຕື້", "ພັນຕື້"),
    ("ລ້ານຕື້", "ລ້ານຕື້", "ລ້ານຕື້"),
    ("ຕຣິລຽນ", "ຕຣິລຽນ", "ຕຣິລຽນ"),
    ("ພັນຕຣິລຽນ", "ພັນຕຣິລຽນ", "ພັນຕຣິລຽນ"),
    ("ລ້ານຕຣິລຽນ", "ລ້ານຕຣິລຽນ", "ລ້ານຕຣິລຽນ"),
]

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
    if power_index == 0:
        return ""
    elif number == 1:
        return _powers[power_index][0]
    elif number > 1:
        return _powers[power_index][1]
    else:
        return _powers[power_index][2]

def convert(number):
    if number == 0:
        return "ສູນ"

    if number < 0:
        return "ລົບ " + convert(-number)

    parts = []
    power_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            power = get_power(number % 1000, power_index)
            if power:
                part += power
            parts.append(part)
        number //= 1000
        power_index += 1

    return "".join(reversed(parts))