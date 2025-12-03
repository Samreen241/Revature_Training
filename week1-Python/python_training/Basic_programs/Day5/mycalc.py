from my_package.interest_calculations import simple_interest
from my_package.mensuration_formulas import area_of_circle, area_of_rect

prin= float(input('Principal: '))
ny= float(input('Years: '))
roi= float(input('Rate of Interest: '))

print(f'Simple Interest:  {simple_interest(1000,1,5)[0]}:'f' Amount : {simple_interest(prin=prin, ny=ny, roi=roi)[1]}')

print(f' Area of circle: {area_of_circle(10)}\n' f'Area of rect : {area_of_rect(10,5)}')
