class romanToInt():
    def __init__(self):
        pass
    
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }


    def roman_to_int(self, roman_string: str) -> int:
        if not isinstance(roman_string, str):
            raise TypeError("Roman number input must be a string")
        
        total = 0 
        roman_string = roman_string.upper()
        # set starting point
        prev_value = self.roman[roman_string[0]]
                
        for n, i in enumerate(range(len(roman_string))):
            cur_value = self.roman.get(roman_string[i])
            print(f'Cur value: {cur_value}')
            
            if cur_value > prev_value:
                total += cur_value - 2 * prev_value
            else:
                total += cur_value
            prev_value = cur_value
            print(f'Total at iterration {n}: {total}')
            
        return print(f'Roman number {roman_string} converted to: {total}')
    
    def int_to_roman(self, n):
        val = [
            1000, 900, 500, 400,
            100, 90,  50,  40,
            10,  9,   5,   4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman = ""
        for i in range(len(val)):
            count = n // val[i]
            roman += syms[i] * count
            n -= val[i] * count
        return print(roman)


if __name__ == "__main__":
    
    converter = romanToInt()
    
    input_1 = "IX" # 9
    input_2 = "III"
    input_3 = "CDXLIII" # 443
    input_4 = 9
       
    converter.roman_to_int(input_2)
    converter.int_to_roman(input_4)
