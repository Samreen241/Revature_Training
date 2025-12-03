
def calculate(m1,m2,m3):
    total=m1,m2,m3
    avg=total/3
    return total,avg

sname=input("Enter your name: ")
m1=int(input("Enter your first number: "))
m2=int(input("Enter your second number: "))
m3=int(input("Enter your third number: "))
tot,avg=calculate(m1,m2,m3)
print(f'Total:{tot}Avg={avg}')


