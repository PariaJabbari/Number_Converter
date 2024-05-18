

def convert_to_persian(num: int) -> str:

    # region validation
    if not isinstance(num, int):
        raise TypeError("Type Error")

    if len(str(num)) > 100:
        raise ValueError("Value Error")
    # endregion

    # region config
    num, is_negative = (-num, True) if num < 0 else (num, False)

    UNIT = {
        0: "",
        1: "هزار",
        2: "میلیون",
        3: "میلیارد",
        4: "بیلیون",
        5: "بیلیارد",
        6: "تریلیون",
        7: "ترلیارد",
        8: "کوآدریلیون",
        9: "کادریلیارد",
        10: "کوینتیلیون",
        11: "کوانتینیارد",
        12: "سکستیلیون",
        13: "سکستیلیارد",
        14: "سپتیلیون",
        15: "سپتیلیارد",
        16: "اکتیلیون",
        17: "اکتیلیارد",
        18: "نانیلیون",
        19: "نانیلیارد",
        20: "دسیلیون",
        21: "دسیلیارد",
        22: "آندسیلیون",
        23: "آندسیلیارد",
        24: "دودسیلیون",
        25: "دودسیلیارد",
        26: "تریدسیلیون",
        27: "تریدسیلیارد",
        28: "کوادردسیلیون",
        29: "کوادردسیلیارد",
        30: "کویندسیلیون",
        31: "کویندسیلیارد",
        32: "سیدسیلیون",
        33: "سیدسیلیارد",
        34: "گوگول",
    }
    # endregion

    def convert_3digit_number(num: int) -> str:
        # region config
        ZERO_NINETEEN = {
            "00": "",
            "01": "یک",
            "02": "دو",
            "03": "سه",
            "04": "چهار",
            "05": "پنج",
            "06": "شش",
            "07": "هفت",
            "08": "هشت",
            "09": "نه",
            "10": "ده",
            "11": "یازده",
            "12": "دوازده",
            "13": "سیزده",
            "14": "چهارده",
            "15": "پانزده",
            "16": "شانزده",
            "17": "هفده",
            "18": "هجده",
            "19": "نوزده",
        }

        TWENTY_NINETY = {
            "0": "",
            "1": "",
            "2": "بیست",
            "3": "سی",
            "4": "چهل",
            "5": "پنجاه",
            "6": "شصت",
            "7": "هفتاد",
            "8": "هشتاد",
            "9": "نود",
        }

        HUNDRED_NINEHUNDRED = {
            "1": "یکصد",
            "2": "دویست",
            "3": "سیصد",
            "4": "چهارصد",
            "5": "پانصد",
            "6": "ششصد",
            "7": "هفتصد",
            "8": "هشتصد",
            "9": "نهصد",
        }
        # endregion

        str_num = str(num).zfill(3)

        first_digit = str_num[0]
        middle_digit = str_num[1]
        last_two_digit = str_num[-2:]
        last_digit = str_num[2]

        res = []

        if first_digit in HUNDRED_NINEHUNDRED:
            res.append(HUNDRED_NINEHUNDRED[first_digit])

        if last_two_digit in ZERO_NINETEEN:
            if last_two_digit != "00":
                res.append(ZERO_NINETEEN[last_two_digit])
        else:
            res.append(f"{TWENTY_NINETY[middle_digit]}{"و" if last_digit != "0" else ""}{\
                ZERO_NINETEEN[f"0{last_digit}"]}")

        return "و".join(res)

    res = []

    for index, three_digit in enumerate(map(int, reversed(f"{num:,}".split(",")))):
        if three_digit != 0:
            res.insert(0, f"{convert_3digit_number(three_digit)}{UNIT[index]}")

    return f"{"منفی" if is_negative else ""}{"و". join(res)}"


print(convert_to_persian(-120000003))
