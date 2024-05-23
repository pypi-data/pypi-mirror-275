_ones= ["", "ஒன்று", "இரண்டு", "மூன்று", "நான்கு", "ஐந்து", "ஆறு", "ஏழு", "எட்டு", "ஒன்பது"]
_teens = ["பத்து", "பதினொன்று", "பன்னிரண்டு", "பதின்மூன்று", "பதினான்கு", "பதினைந்து", "பதினாறு", "பதினேழு", "பதினெட்டு", "பத்தொன்பது"] 
_tens = ["", "", "இருபது", "முப்பது", "நாற்பது", "ஐம்பது", "அறுபது", "எழுபது", "எண்பது", "தொண்ணூறு"]
_hundreds = ["", "நூறு", "இருநூறு", "முந்நூறு", "நாநூறு", "ஐநூறு", "அறுநூறு", "எழுநூறு", "எண்ணூறு", "தொள்ளாயிரம்"]

_scales = [
    ("", "", ""),
    ("ஆயிரம்", "ஆயிரம்", "ஆயிரம்"),
    ("மில்லியன்", "மில்லியன்", "மில்லியன்"),
    ("பில்லியன்", "பில்லியன்", "பில்லியன்"),
    ("டிரில்லியன்", "டிரில்லியன்", "டிரில்லியன்"),
    ("குவாட்ரில்லியன்", "குவாட்ரில்லியன்", "குவாட்ரில்லியன்"),
    ("குவின்டில்லியன்", "குவின்டில்லியன்", "குவின்டில்லியன்"),
    ("செக்ஸ்டில்லியன்", "செக்ஸ்டில்லியன்", "செக்ஸ்டில்லியன்"),
    ("செப்டில்லியன்", "செப்டில்லியன்", "செப்டில்லியன்"),
    ("ஒக்டில்லியன்", "ஒக்டில்லியன்", "ஒக்டில்லியன்"),
    ("நானில்லியன்", "நானில்லியன்", "நானில்லியன்"),
    ("டெசில்லியன்", "டெசில்லியன்", "டெசில்லியன்"),
]

_fractions = {
    2: 'அரை',
    3: 'முக்கால்',
    4: 'கால்',
    5: 'ஐந்தில் ஒன்று',
    6: 'ஆறில் ஒன்று',
    7: 'ஏழில் ஒன்று',
    8: 'எட்டில் ஒன்று',
    9: 'ஒன்பதில் ஒன்று',
    10: 'பத்தில் ஒன்று',
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
            return _tens[tens] + " " + _ones[ones]
    else:
        hundreds, less_than_hundred = divmod(number, 100)
        if less_than_hundred == 0:
            return _hundreds[hundreds]
        else:
            return _hundreds[hundreds] + " " + convert_less_than_thousand(less_than_hundred)

def get_scale(number, scale_index):
    if scale_index == 0:
        return ""
    elif number == 1:
        return _scales[scale_index][0]
    else:
        return _scales[scale_index][1]

def convert_fraction(numerator, denominator):
    if numerator == 1:
        return _fractions[denominator]
    else:
        return convert(numerator) + " " + _fractions[denominator]

def convert(number):
    if isinstance(number, float):
        integer_part = int(number)
        fraction_part = round(number - integer_part, 10)

        integer_words = convert(integer_part)
        fraction_words = convert_fraction(int(fraction_part * 10), 10)

        return f"{integer_words} புள்ளி {fraction_words}"

    if number == 0:
        return "பூஜ்ஜியம்"

    if number < 0:
        return "எதிர்மறை " + convert(-number)

    parts = []
    scale_index = 0
    while number > 0:
        if number % 1000 != 0:
            part = convert_less_than_thousand(number % 1000)
            scale = get_scale(number % 1000, scale_index)
            if scale:
                part += " " + scale
            parts.append(part)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(parts))