
class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary

    def initialize(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        self.real += other.real
        self.imaginary += other.imaginary

    def subtract(self, other):
        self.real -= other.real
        self.imaginary -= other.imaginary

    def multiply(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        self.real = real_part
        self.imaginary = imaginary_part

    def divide(self, other):
        if other.real == 0 and other.imaginary == 0:
            print("Error: Division by zero is not allowed.")
            return
        denom = other.real ** 2 + other.imaginary ** 2
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denom
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denom
        self.real = real_part
        self.imaginary = imaginary_part
        print(f"After division: {self}")

    def modulus(self):
        mod = (self.real ** 2 + self.imaginary ** 2) ** 0.5
        print(f"Modulus: {mod}")

    def conjugate(self):
        self.imaginary = -self.imaginary
        print(f"Conjugate: {self}")

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {-self.imaginary}i"

complex_num = ComplexNumber()
first_initialization = True



while True:
    try:
        s = input().split()
        if s[0] == 'exit':
            break

        if s[0] == 'initialize':
            a = s[1].split(',')
            complex_num.initialize(float(a[0]), float(a[1]))
            if first_initialization:
                print(f"Initialized: {complex_num}")
                first_initialization = False

        elif s[0] == 'add':
            a = s[1].split(',')
            other = ComplexNumber(float(a[0]), float(a[1]))
            complex_num.add(other)
            print(f"After addition: {complex_num}")

        elif s[0] == 'subtract':
            a = s[1].split(',')
            other = ComplexNumber(float(a[0]), float(a[1]))
            complex_num.subtract(other)
            print(f"After subtraction: {complex_num}")

        elif s[0] == 'multiply':
            a = s[1].split(',')
            other = ComplexNumber(float(a[0]), float(a[1]))
            complex_num.multiply(other)
            print(f"After multiplication: {complex_num}")

        elif s[0] == 'divide':
            a = s[1].split(',')
            other = ComplexNumber(float(a[0]), float(a[1]))
            complex_num.divide(other)

        elif s[0] == 'modulus':
            complex_num.modulus()

        elif s[0] == 'conjugate':
            complex_num.conjugate()

    except Exception as e:
        break
