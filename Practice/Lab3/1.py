class printContent:
    String1 = ""

    def __init__(self, String1):
        self.String1 = String1
    def getString(self):
        res = "Hello " + self.String1 + "!"
        return res

    def printString():
        print(self.String1)
        return


name = input()

obj = printContent(name)    

obj.getString()
obj.printString()
