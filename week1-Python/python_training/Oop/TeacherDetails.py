from Oop.College import College

class TeacherDetails(College):
    def __init__(self,ccode,cname,empid,tname,dept):
        College.__init__(self, ccode,cname)
        self.empid=empid
        self.tname=tname
        self.dept=dept

    def display(self):
        print(f'{self.ccode} \t  {self.cname} \n' 
              f'{self.empid} \n {self.tname} \n {self.dept}')

