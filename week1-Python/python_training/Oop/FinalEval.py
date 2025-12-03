from StudExcurr import StudExcurr
from TeacherDetails import TeacherDetails

class FinalEval(StudExcurr, TeacherDetails):
    def __init__(self, ccode, cname, rollno, sname, m1, m2, m3,exm1, exm2, empid, tname, dept, feedbackfromteacher):
        StudExcurr.__init__(self,ccode, cname, rollno, sname, m1, m2, m3, exm1, exm2)
        TeacherDetails.__init__(self,ccode, cname,empid, tname, dept)

        self.feedbackfromteacher = feedbackfromteacher