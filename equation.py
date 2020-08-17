import fraction


class Equation:

    def __init__(self, equation):
        self.__equation = equation
        list1 = equation.split()
        self.__frac1 = list1[0]
        self.__operator = list1[1]
        self.__frac2 = list1[2]

    def __str__(self):
        return str(self.__frac1) + " " + str(self.__operator) + " " + str(self.__frac2)

    def split(self):
        self_str = str(self)
        self_list = self_str.split(" ")
        return self_list

    def create_frac(self, frac1, frac2):
        str_frac1 = str(frac1)
        list1 = str_frac1.split("/")
        frac1 = fraction.Fraction(list1[0], list1[1])
        str_frac2 = str(frac2)
        list2 = str_frac2.split("/")
        frac2 = fraction.Fraction(list2[0], list2[1])
        return frac1, frac2

    def calculate(self):
        frac1_object, frac2_object = self.create_frac(self.__frac1, self.__frac2)
        if self.__operator == '+':
            answer = frac1_object.addition(frac2_object)
        elif self.__operator == '-':
            answer = frac1_object.subtract(frac2_object)
        elif self.__operator == '*':
            answer = frac1_object.multiply(frac2_object)
        elif self.__operator == '/':
            answer = frac1_object.divide(frac2_object)
        else:
            answer = "invalid equation"
        return answer