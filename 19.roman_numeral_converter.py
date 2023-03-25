# Bu proje, sayıları Roma rakamlarına ve Roma rakamlarını sayılara dönüştüren bir program oluşturmayı içerir.
# (This project involves creating a program that converts numbers to Roman numerals and vice versa.)

def roman_to_int(roman_numeral):
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    prev_value = 0
    for char in roman_numeral:
        current_value = roman_dict[char]
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value
    return total


roman_numeral = input("Please enter a Roman numeral: ")
if not all(char in "IVXLCDM" for char in roman_numeral):
    print("Please enter a valid Roman numeral.")
else:
    integer = roman_to_int(roman_numeral)
    print(f"{roman_numeral} = {integer}")
