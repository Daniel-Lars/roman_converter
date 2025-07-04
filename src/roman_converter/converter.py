import logging

from roman_converter.custom_errors import InvalidIntegerError

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    style="%",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class RomanToInt:
    def __init__(self):
        self.roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def roman_to_int(self, roman_string: str) -> int:
        if not isinstance(roman_string, str):
            raise TypeError("Roman number input must be a string")

        total = 0
        roman_string = roman_string.upper()
        # set starting point
        prev_value = self.roman[roman_string[0]]
        logging.debug("Starting conversion of Roman numeral to integer.")
        for n, i in enumerate(range(len(roman_string))):
            cur_value = self.roman.get(roman_string[i])
            logging.debug("Cur value: %s,", cur_value)

            if cur_value > prev_value:
                total += cur_value - 2 * prev_value
            else:
                total += cur_value
            prev_value = cur_value

        return total

    def int_to_roman(self, n):
        if not isinstance(n, int):
            raise InvalidIntegerError(n)

        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = ""
        for i in range(len(val)):
            count = n // val[i]
            result += syms[i] * count
            n -= val[i] * count
        return result


if __name__ == "__main__":
    converter = RomanToInt()
    print(converter.roman_to_int("XII"))  # Example usage
    print(converter.int_to_roman(12))  # Example usage
    # Add more test cases as needed
