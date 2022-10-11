"""
Написать функцию, которая принимает на вход строку - римское число, а возвращает это число в арабском виде. Например,
если передаём "XV" - должна вернуть 15, если передаём "IV" - должна вернуть 4.
"""

romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
result = 0
roman = 'XXIXI'
for i, c in enumerate(roman):
    if romans[roman[i]] < romans[roman[i]]:
        result -= romans[roman[i]]
    else:
        result += romans[roman[i]]

print(result)
