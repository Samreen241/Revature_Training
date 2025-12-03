from ArithCalculations import ArithCalculations

n1= int(input())
n2= int(input())

calc=ArithCalculations(n1,n2)

print(f'{calc.add()}')
print(f'{calc.sub()}')
print(f'{calc.mul()}')
print(f'{calc.div()}')

try:
    l1=[1,5,7,3]
    val=l1[2]
    res=calc.div()
except ZeroDivisionError:
    print('0 in denominator')
else:
    print(val)
    print(res)
finally:
    print('Very good keep it up *****!!')