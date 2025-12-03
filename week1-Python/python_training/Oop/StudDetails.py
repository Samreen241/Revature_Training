from Basic_programs.Day4.optional_parameters import sname
from Oop.College import College


class StudentDetail:
    def __init__(self, ccode, cname, rollno,name,m1,m2,m3):
        College. __init__(self,ccode, cname)
        self.rollno = rollno
        self.cname = cname
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def get_rollno(self):
        return self.rollno

    def get_rollno(self, rollno):
        self.rollno = rollno

    def get_sname(self):
        self.sname = sname

    def get_sname(self, sname):
        self.sname = sname

    def get_m1(self):
        return self.m1

    def get_m1(self, m1):
        self.m1 = m1

    def get_m2(self):
        return self.m2

    def get_m2(self,m2):
        self.m2 = m2

    def get_m3(self):
        return self.m3

    def get_m3(self, m3):
        self.m3 = m3


    def get_cname(self):
        return self.cname

    def calc_tot(self):
        return self.m1 + self.m2 +self.m3

    def calc_avg(self):
        return self.calc_tot() / 3