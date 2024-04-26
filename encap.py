class Calcu:
    def __sum(self):
        a = int(input ("Enter first number : "))
        b =  int(input("Enter second number : "))
        sumResult = a+b
        print(f"Sum of {sumResult}")
        
class Calcula(Calcu):
    def _sub(self, a, b):
            self.a = a
            self.b = b
            Subresult = (a-b)
            print(f("Subtraction of {Subresult}"))
        
        
obj=Calcu()
obj=Calcula()
obj._Calcu__sum()