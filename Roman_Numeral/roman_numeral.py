class RomanNumeral:

    def __init__(self):
        self.roman_numerals = {
            "MMM":3000, "MM":2000, "M":1000,
            "CM":900, "DCCC":800, "DCC":700, "DC":600, "D":500, "CD":400, "CCC":300, "CC":200, "C":100,
            "XC":90, "LXXX":80, "LXX":70, "LX":60, "L":50, "XL":40, "XXX":30, "XX":20, "X":10,
            "IX":9, "VIII":8, "VII":7, "VI":6, "V":5, "IV":4 ,"III":3, "II":2, "I":1
            }
        

    def return_string_from_roman_numerals(self, number_to_search):
        string_to_return =''
        for key,value in self.roman_numerals.items():
            if value == number_to_search:
                string_to_return = key

        return string_to_return
        
    def return_thousands_of_a_number(self, number):
        find_dict_key_to_return = (number // 1000) * 1000
        string_to_return = self.return_string_from_roman_numerals(find_dict_key_to_return)

        return string_to_return
    
    def return_hundreds_of_a_number(self, number):
        hundreds = number % 1000
        find_dict_key_to_return = (hundreds // 100) * 100
        string_to_return = self.return_string_from_roman_numerals(find_dict_key_to_return)

        return string_to_return
        
    def return_tens_of_a_number(self, number):
        tens = number % 100
        find_dict_key_to_return = (tens // 10) * 10
        string_to_return = self.return_string_from_roman_numerals(find_dict_key_to_return)
        
        return string_to_return

    def return_units_of_a_number(self, number):
        units = number % 10
        string_to_return = self.return_string_from_roman_numerals(units)

        return string_to_return
    
    def convert_integer_into_roman_numeral(self, number):
        roman_numeral_to_return = self.return_thousands_of_a_number(number) 
        roman_numeral_to_return += self.return_hundreds_of_a_number(number)
        roman_numeral_to_return += self.return_tens_of_a_number(number)
        roman_numeral_to_return += self.return_units_of_a_number(number)

        return roman_numeral_to_return
    
    def user_feedback(self, number):
        converted_number_to_string = self.convert_integer_into_roman_numeral(number)
        message = f"For your number {number} the Roman Numeral convert is {converted_number_to_string}"
        
        return message