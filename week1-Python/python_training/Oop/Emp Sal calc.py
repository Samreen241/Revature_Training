from Oop.Employee import Employee

employee= Employee()

empid=int(input('Emp id: '))
ename=input('E Name: ')
bp=float(input('Basic Pay: '))

print(f'Emp id: {empid}\n Name: {ename}\n' f'Gross Pay: {employee.calc_grosspay(bp)}\n'f'Net Pay: {employee.calc_netpay(bp)}')

