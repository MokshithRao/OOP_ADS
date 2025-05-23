class ComplexNumber:
    def __init__(self):
        self.real = 0.0
        self.imaginary = 0.0

    def initialize(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)
        print(f"Initialized: {self}")



    def add(self, other):
        self.real += float(other[0])
        self.imaginary += float(other[1])
        print(f"After addition: {self}")


    def subtract(self, other):
        self.real -= float(other[0])
        self.imaginary -= float(other[1])
        print(f"After subtraction: {self}")



    def multiply(self, other):
        real_part = self.real * float(other[0]) - self.imaginary * float(other[1])
        imaginary_part = self.real * float(other[1]) + self.imaginary * float(other[0])
        self.real = real_part
        self.imaginary = imaginary_part
        print(f"After multiplication: {self}")

    def divide(self, other):
        other[0] = float(other[0])
        other[1] = float(other[1])
        denominator = other[0] ** 2 + other[1] ** 2

        if denominator == 0:
            print("Error: Division by zero is not allowed.")
            return
        
        real_part = (self.real * other[0] + self.imaginary * other[1]) / denominator
        imaginary_part = (self.imaginary * other[0] - self.real * other[1]) / denominator
        self.real = real_part
        self.imaginary = imaginary_part
        print(f"After division: {self}")



    def modulus(self):
        r = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        print(f"Modulus: {r}")



    def conjugate(self):
        self.imaginary = - self.imaginary
        print(f"Conjugate: {self}")


    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"


    def main_run(self):

        while True:
            try:
                s = input().split()

                if s[0] == 'exit':
                    break

                if s[0] == 'initialize':
                    a = s[1].split(',')
                    self.initialize(a[0], a[1])
        
                elif s[0] == 'add':
                    a = s[1].split(',')
                    self.add(a)
                
                elif s[0] == 'subtract':
                    a = s[1].split(',')
                    self.subtract(a)

                elif s[0] == 'multiply':
                    a = s[1].split(',')
                    self.multiply(a)

                elif s[0] == 'divide':
                    a = s[1].split(',')
                    self.divide(a)
                    
                elif s[0] == 'modulus':
                    a = s[1].split(',')
                    self.modulus()

                elif s[0] == 'conjugate':
                    a = s[1].split(',')
                    self.conjugate()
                    

            except:
                break
                


if __name__ == '__main__':
    complex_num = ComplexNumber()
    complex_num.main_run()



