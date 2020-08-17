import equation

def read_equation():
    user_input = input(
        "Enter an equation(separate fraction with / no spaces and separate fraction from operator with space")
    equation_input = equation.Equation(user_input)
    return equation_input


def read_equation2(answer):
    answer = str(answer)
    user_input = input()
    raw_equation = answer + " " + user_input
    equation_input = equation.Equation(raw_equation)
    return equation_input


def main():
    equation_input = read_equation()
    answer = equation_input.calculate()
    print(answer)
    go = input('Continue? q to quit c to clear')
    while go != 'q':
        if go == 'c':
            equation_input = read_equation()
            answer = equation_input.calculate()
            print(answer)
            go = input('Continue? q to quit c to clear')
        else:
            equation_input = read_equation2(answer)
            answer = equation_input.calculate()
            print(answer)
            go = input('Continue? q to quit c to clear')


main()
