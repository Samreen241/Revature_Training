from StudDetails import StudentDetail

class StudExcurr(StudentDetail):
    def __init__(self,ccode,cname,rollno, sname, m1,m2, m3,exm1,exm2):
        StudentDetail.__init__(self, ccode,cname,rollno,sname,m1,m2, m3)
        self.exm1=exm1
        self.exm2=exm2

    def calc_extot(self):
        return self.exm1+self.exm2