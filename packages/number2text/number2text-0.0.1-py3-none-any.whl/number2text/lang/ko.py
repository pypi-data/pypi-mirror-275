_ones= ["", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
_tens = ["", "십", "이십", "삼십", "사십", "오십", "육십", "칠십", "팔십", "구십"]
_hundreds = ["", "백", "이백", "삼백", "사백", "오백", "육백", "칠백", "팔백", "구백"]
_thousands = ["", "천", "이천", "삼천", "사천", "오천", "육천", "칠천", "팔천", "구천"]

_scales = [
    ("", "", ""),
    ("만", "만", "만"),
    ("억", "억", "억"),
    ("조", "조", "조"),
    ("경", "경", "경"),
    ("해", "해", "해"),
    ("자", "자", "자"),
    ("양", "양", "양"),
    ("구", "구", "구"),
    ("간", "간", "간"),
    ("정", "정", "정"),
    ("재", "재", "재"),
    ("극", "극", "극"),
    ("항하사", "항하사", "항하사"),
    ("아승기", "아승기", "아승기"),
    ("나유타", "나유타", "나유타"),
    ("불가사의", "불가사의", "불가사의"),
    ("무량대수", "무량대수", "무량대수")
]

def convert_less_than_ten_thousand(number):
    if number < 10:
        return _ones[number]
    elif number < 100:
        tens, ones = divmod(number, 10)
        return _tens[tens] + " " + _ones[ones] if ones > 0 else _tens[tens]
    elif number < 1000:
        hundreds, less_than_hundred = divmod(number, 100)
        return _hundreds[hundreds] + " " + convert_less_than_ten_thousand(less_than_hundred) if less_than_hundred > 0 else _hundreds[hundreds]
    else:
        thousands, less_than_thousand = divmod(number, 1000)
        return _thousands[thousands] + " " + convert_less_than_ten_thousand(less_than_thousand) if less_than_thousand > 0 else _thousands[thousands]

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    elif number < 1000000:
        return _scales[scale_index][1] 
    else:
        return _scales[scale_index][2]

def convert(number):
    if number == 0:
        return "영"

    if number < 0:
        return "마이너스 " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 10000 != 0:
            part = convert_less_than_ten_thousand(number % 10000)
            scale = get_scale(number % 10000, scale_index)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 10000
        scale_index += 1

    return " ".join(reversed(parts))