class RomanNumeral:

    def __init__(self):
        self.roman_numerals = {
            "M":1000,
            "CM":900,"DCCC":800,"DCC":700,"DC":600,"D":500,"CD":400,"CCC":300,"CC":200,"C":100,
            "XC":90,"LXXX":80,"LXX":70,"LX":60,"L":50,"XL":40,"XXX":30,"XX":20,"X":10,
            "IX":9,"VIII":8,"VII":7,"VI":6,"V":5,"IV":4,"III":3,"II":2,"I":1
            }
        

    def return_string_from_roman_numerals(self,number_to_search):
        for key,value in self.roman_numerals.items():
            if value == number_to_search:
                string_to_return = key

        return string_to_return
        
    def return_thousands_of_a_number(self,number):
        string_to_return = ''
        thousands = number // 1000
        
        return string_to_return + 'M' * thousands
    
    def return_hundreds_of_a_number(self,number):
        hundreds = number % 1000
        find_dict_key_to_return = (hundreds // 100) * 100
        string_to_return = self.return_string_from_roman_numerals(find_dict_key_to_return)

        return string_to_return
        
    def return_tens_of_a_number(self,number):
        tens = number % 100
        find_dict_key_to_return = (tens // 10) * 10
        string_to_return = self.return_string_from_roman_numerals(find_dict_key_to_return)
        return string_to_return










