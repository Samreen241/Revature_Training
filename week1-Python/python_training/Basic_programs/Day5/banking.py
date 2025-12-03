""" Banking Interest Calculations"""

from interest_calculations import simple_interest, compound_interest

prin= float(input('Principal: '))
ny= float(input('Years: '))
roi= float(input('Rate of Interest: '))
si,amt= simple_interest(prin=prin, ny=ny, roi=roi)
print(f'SI: {si}, Amount: {amt}')

amt= compound_interest(prin=prin, ny=ny, roi=roi)
print(f'Amount: {amt}')

