_ones= ["", "אחת", "שתיים", "שלוש", "ארבע", "חמש", "שש", "שבע", "שמונה", "תשע"]
_teens = ["עשר", "אחת עשרה", "שתים עשרה", "שלוש עשרה", "ארבע עשרה", "חמש עשרה", "שש עשרה", "שבע עשרה", "שמונה עשרה", "תשע עשרה"]
_tens = ["", "", "עשרים", "שלושים", "ארבעים", "חמישים", "שישים", "שבעים", "שמונים", "תשעים"]
_hundreds = ["", "מאה", "מאתיים", "שלוש מאות", "ארבע מאות", "חמש מאות", "שש מאות", "שבע מאות", "שמונה מאות", "תשע מאות"]

_scales = [
    ("", "", ""),
    ("אלף", "אלפיים", "אלפים"),
    ("מיליון", "שני מיליון", "מיליונים"),
    ("מיליארד", "שני מיליארד", "מיליארדים"),
    ("טריליון", "שני טריליון", "טריליונים"),
    ("קוודריליון", "שני קוודריליון", "קוודריליונים"),
    ("קווינטיליון", "שני קווינטיליון", "קווינטיליונים"),
    ("סקסטיליון", "שני סקסטיליון", "סקסטיליונים"),
    ("ספטיליון", "שני ספטיליון", "ספטיליונים"),
    ("אוקטיליון", "שני אוקטיליון", "אוקטיליונים"),
    ("נוניליון", "שני נוניליון", "נוניליונים"),
    ("דציליון", "שני דציליון", "דציליונים"),
]

_fractions = {
    2: 'חצי',
    3: 'שליש',
    4: 'רבע',
    5: 'חמישית',
    6: 'שישית',
    7: 'שביעית',
    8: 'שמינית',
    9: 'תשיעית',
    10: 'עשירית',
}

def convert_less_than_thousand(number, is_female):
    if number < 10:
        return _ones[number] if is_female else _ones[number][:-1]
    elif number < 20:
        return _teens[number - 10]
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return _tens[tens]
        else:
            return _tens[tens] + " ו" + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " ו" + convert_less_than_thousand(less_than_hundred, is_female)

def get_scale(number, scale_index, is_female):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0] if is_female else _scales[scale_index][1] 
    elif number == 2:
        return _scales[scale_index][1]
    else:
        return _scales[scale_index][2]

def convert_fraction(numerator, denominator, is_female):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator, is_female) + " " + _fractions[denominator]

def convert(number, is_female=True):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part, is_female)
        fraction_words = convert_fraction(int(fraction_part * 10), 10, is_female)

        return f"{integer_words} ו{fraction_words}"

    if number == 0:
        return "אפס"

    if number < 0:
        return "מינוס " + convert(-number, is_female)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000, is_female)
            scale = get_scale(number % 1000, scale_index, is_female)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))