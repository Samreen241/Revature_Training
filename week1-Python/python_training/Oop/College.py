class College:
    def __init__(self, ccode, cname):
        self.ccode = ccode
        self.cname = cname

    def get_code(self):
        return self._ccode

    def get_cname(self):
        return self._cname

    def display(self):
        return self._ccode, self._cname