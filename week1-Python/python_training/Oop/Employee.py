class Employee:
    def calc_allowance(selfself, bp):
        return (bp * 0.1)+ (bp * 0.05)

    def cal_ded(selfself, bp):
        return bp * 0.03

    def calc_grosspay(self, bp):
        return bp + self.calc_allowance(bp)

    def calc_netpay(self, bp):
        return  self.calc_grosspay(bp)-self.cal_ded(bp)

