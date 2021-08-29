class RomanNumerals:
    @staticmethod
    def to_roman(num):
        roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                 "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        rez = ""
        for key, value in roman.items():
            times = num // value
            num = num % value
            rez += key*times
        return rez

    @staticmethod
    def from_roman(s):
        roman = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                 "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        rez = 0
        for key, value in roman.items():
            while s[:len(key)] == key:
                rez += value
                s = s[len(key):]
        return rez
