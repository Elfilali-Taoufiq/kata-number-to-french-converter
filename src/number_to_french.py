basic_numbers_mapping = {
    0: "zéro",
    1: "un",
    2: "deux",
    3: "trois",
    4: "quatre",
    5: "cinq",
    6: "six",
    7: "sept",
    8: "huit",
    9: "neuf",
    10: "dix",
    11: "onze",
    12: "douze",
    13: "treize",
    14: "quatorze",
    15: "quinze",
    16: "seize",
    17: "dix-sept",
    18: "dix-huit",
    19: "dix-neuf",
    20: "vingt",
    30: "trente",
    40: "quarante",
    50: "cinquante",
    60: "soixante",
    70: "soixante-dix",
    80: "quatre-vingt",
    90: "quatre-vingt-dix",
    100: "cent",
    1000: "mille"
}

THEN = 10
HUNDRED = 100
THOUSAND = 1000
MILLION = 1000000
SPLITER = "-"
PLURAL_S = 's'


def convert_number_to_french(number):
    if number in basic_numbers_mapping:
        return basic_numbers_mapping[number]

    elif number <= HUNDRED:
        return convert_tens_to_french(number=number)

    elif number < THOUSAND:
        return convert_hundreds_to_french(number=number)

    elif number < MILLION:
        return convert_thousands_to_french(number=number)

    else:
        raise ValueError("This script currently supports numbers up to 999999.")


def convert_hundreds_to_french(number):
    quotient, reminder = divmod(number, HUNDRED)
    quotient = '' if quotient == 1 else convert_number_to_french(quotient)
    return (f"{quotient}{SPLITER if quotient else ''}cent{PLURAL_S if not reminder else ''}"
            f"{SPLITER if reminder else ''}{convert_number_to_french(reminder) if reminder else ''}")


def convert_thousands_to_french(number):
    quotient, reminder = divmod(number, THOUSAND)
    quotient = '' if quotient == 1 else convert_number_to_french(quotient)
    return (f"{quotient}{SPLITER if quotient else ''}mille{PLURAL_S if not reminder else ''}"
            f"{SPLITER if reminder else ''}{convert_number_to_french(reminder) if reminder else ''}")


def convert_tens_to_french(number):
    quotient, reminder = divmod(number, THEN)
    if quotient == 7 or quotient == 9:
        quotient = quotient - 1
        return f"{basic_numbers_mapping[quotient * THEN]}-{basic_numbers_mapping[reminder + THEN]}"
    if reminder > 1:
        return f"{basic_numbers_mapping[quotient * THEN]}-{basic_numbers_mapping[reminder]}"
    elif reminder == 1:
        return f"{basic_numbers_mapping[quotient * THEN]}-et-{basic_numbers_mapping[reminder]}"
    else:
        return f"{basic_numbers_mapping[quotient * THEN]}"


if __name__ == '__main__':
    input_list = [10000]

    converted_numbers = list(map(convert_number_to_french, input_list))
    print(converted_numbers)
