class Fraction:

    def __init__(self, num, denom):
        self.__num = int(num)
        self.__denom = int(denom)
        self.__num, self.__denom = self.reduce()

    def reduce(self):
        factor = self.gcf()
        num = self.__num // factor
        denom = self.__denom // factor
        return num, denom

    def gcf(self):
        i = int(self.__num)
        while i > 0:
            if self.__denom % i == 0 and self.__num % i == 0:
                factor = i
                return factor
            else:
                i -= 1
        return 1

    def __str__(self):
        return str(self.__num) + "/" + str(self.__denom)

    def addition(self, frac2):
        num1 = self.__num * frac2.__denom
        num2 = frac2.__num * self.__denom
        denom = self.__denom * frac2.__denom
        num_sum = num1 + num2
        answer = Fraction(num_sum, denom)
        return answer

    def subtract(self, frac2):
        num1 = self.__num * frac2.__denom
        num2 = frac2.__num * self.__denom
        denom = self.__denom * frac2.__denom
        num_ans = num1 - num2
        answer = Fraction(num_ans, denom)
        return answer

    def multiply(self, frac2):
        num = self.__num * frac2.__num
        denom = self.__denom * frac2.__denom
        answer = Fraction(num, denom)
        return answer

    def divide(self, frac2):
        num = self.__num * frac2.__denom
        denom = self.__denom * frac2.__num
        answer = Fraction(num, denom)
        return answer

    def read(self):
        return self.__num + "/" + self.__denom