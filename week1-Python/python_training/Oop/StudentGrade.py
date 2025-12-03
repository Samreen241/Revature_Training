from StudDetails import StudentDetail

from StudExcurr import StudExcurr
from Oop.TeacherDetails import TeacherDetails

from FinalEval import FinalEval

ccode= int(input('Code: '))
cname = input('Coll Name: ')

rollno = int(input('Roll no: '))
name = input('Name: ')
m1 = int(input('Mark1: '))
m2 = int(input('Mark2: '))
m3 = int(input('Mark3: '))

exm1=int(input('Ex Mark 1: '))
exm2=int(input('Ex Mark 2: '))

'''stud = StudentDetail(ccode, cname, rollno,name,m1,m2,m3,exm1, exm2)

print( f'{stud.rollno} \n {stud.cname} \n {stud.calc_tot()} \n  '
       f'{stud.calc_avg()}')
'''
empid=int(input('Empid: '))
tname=input('Name: ')
dept=input('Dept: ')

'''teacher = TeacherDetails(ccode, cname, empid,tname, dept)
teacher.display()'''

feedbackfromteacher=input('Enter Feedback ')

FinalEval= FinalEval(ccode, cname, rollno, name, m1, m2, m3,exm1, exm2, empid, tname, dept, feedbackfromteacher)

print(f'{FinalEval.display()}\n'
      f'{FinalEval.get_rollno()} \n {FinalEval.sname()}\n'
      f'{FinalEval.calc_avg()} \n {FinalEval.calc_tot()}\n'
      f'{FinalEval.calc_extot()}\n '
      f'{FinalEval.display()}\n' 
      f'{FinalEval.feedbackfromteacher()}')