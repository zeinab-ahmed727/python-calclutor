


def calculate(a, b, operation):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("Both operands must be numbers.")
    
    def sum(a,b):
        return a+b

    
    