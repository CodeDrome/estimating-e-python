import math

E15DP = "2.718281828459045"

RED = "\x1B[31;1m"
GREEN = "\x1B[32;1m"
WHITE = "\x1B[37;1m"
RESET = "\x1B[0m"


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Estimating e  |")
    print("-----------------\n")

    expansion_1()

    expansion_2()

    newtons_series()

    brothers_formula()


def print_as_text(e):

    """
    Takes a value for e and prints it below a definitive value,
    with matching digits in green and non-matching digits in red
    """

    e_string = "{:1.15f}".format(e)

    print("Definitive: " + WHITE + E15DP + RESET)

    print("Estimated:  ", end="")

    for i in range(0, len(e_string)):
        if e_string[i] == E15DP[i]:
            print(GREEN + e_string[i] + RESET, end="")
        else:
            print(RED + e_string[i] + RESET, end="")

    print("\n")


def expansion_1():

    print(WHITE + "First expansion\nn = 100000\n---------------" + RESET)

    n = 100000
    e = (1 + 1/n)**n

    print_as_text(e)


def expansion_2():

    print(WHITE +
          "Second expansion\nn = 0.000000001\n----------------" +
          RESET)

    n = 0.000000001
    e = (1 + n)**(1/n)

    print_as_text(e)


def newtons_series():

    print(WHITE + "Newton's Series\nn = 0 to 12\n---------------" + RESET)

    e = 0

    for n in range(0, 13):
        e += (1 / math.factorial(n))

    print_as_text(e)


def brothers_formula():

    print(WHITE + "Brothers Formula\nn = 0 to 8\n----------------" + RESET)

    e = 0

    for n in range(0, 9):
        e += (2*n + 2) / (math.factorial(2*n + 1))

    print_as_text(e)


main()
