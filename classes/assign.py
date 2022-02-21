class Compute:
    def __init__(self, num1, num2, fn):
        self.num2 = num2
        self.num1 = num1
        self.fn = fn

    def get_data(self):
        num1 = int(input('Enter number1: '))
        self.num1 = num1
        num2 = int(input('Enter number2: '))
        self.num2 = num2
        fn = input('Enter your name: ')
        self.fn = fn

    def display(self):
        if self.num1 > self.num2:
            for i in range(self.num2, self.num1):
                print(f'Hello {self.fn}')
            s = self.num2 + self.num1
            product = self.num1 * self.num2
            print(f'Sum: {s}, Product: {product}')
        else:
            for i in range(self.num1, self.num2):
                print(f'Hello {self.fn}')
            s = self.num1 + self.num2
            product = self.num1 * self.num2
            print(f'Sum: {s}, Product: {product}')


# Instantiation
add = Compute(0, 0, '')
add.get_data()
add.display()
