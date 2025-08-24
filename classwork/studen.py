class student:
    def __init__(self,name,regisno,marks):
        self.name = name 
        self.marks = marks
        self.totalmarks = 500
        self.regisno = regisno

    def getpercent(self) : 
        return sum(marks)/5
    
    def getresult(self): 
        print(self.name, self.regisno,self.getpercent())
marks = [1, 2, 3, 4, 5]
s1 = student("ram", 343, marks)
print(s1.getpercent())
print(s1.getresult())