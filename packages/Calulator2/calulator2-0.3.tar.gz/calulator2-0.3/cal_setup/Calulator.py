class Calculator:
    '''
    Calculator类提供了基本的数学运算功能,包括加法、减法、乘法、除法和幂运算。
    '''

    def add(a, b):
        # 加法
        return a + b

    def subtract(a, b):
        # 减法
        return a - b

    def multiply(a, b):
        # 乘法
        return a * b

    def divide(a, b):
        # 除法
        if b == 0:
            raise ValueError("除数不能为0")
        return a / b

    def power(a, b):
        # 幂运算
        return a**b
