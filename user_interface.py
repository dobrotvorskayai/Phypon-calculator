from mod_calc import mul, summ, div, sub, int_div, rem_of_div, sqrt, exp, mul_comp, summ_comp, div_comp, sub_comp, exp_comp
from exceptions import test

def main_menu():
    while True:
        type = input ("Choose type numbers, please:\n"
                      "1 - rational\n"
                      "2 - complex\n"
                      "0 - exit\n")
        match type:
            case "1":
                menu_rational()
            case "2":
                menu_complex()
            case "0":
                break
            case _:
                print("Enter number from 0 to 2, please")

def menu_rational():
    while True:
        type = input ("Choose action, please:\n"
                      "1 - *\n"
                      "2 - /\n"
                      "3 - //\n"
                      "4 - %\n"
                      "5 - +\n"
                      "6 - -\n"
                      "7 - **\n"
                      "8 - sqrt\n"
                      "0 - previous step\n")
        match type:
            case "1":
                print(mul(rat()))
            case "2":
                print(div(rat()))
            case "3":
                print(int_div(rat()))
            case "4":
                print(rem_of_div(rat()))
            case "5":
                print(summ(rat()))
            case "6":
                print(sub(rat()))
            case "7":
                print(exp(rat()))
            case "8":
                print(sqrt(rat_sqrt()))
            case "0":
                break

            case _:
                print("Enter number from 0 to 8, please")

def menu_complex():
    while True:
        type = input ("Choose action, please:\n"
                      "1 - *\n"
                      "2 - /\n"
                      "3 - +\n"
                      "4 - -\n"
                      "5 - **\n"
                      "6 - sqrt\n"
                      "0 - previous step\n")
        match type:
            case "1":
                print(mul_comp(comp()))
            case "2":
                print(div_comp(comp()))
            case "3":
                print(summ_comp(comp()))
            case "4":
                print(sub_comp(comp()))
            case "5":
                print(exp_comp(comp()))
            case "6":
               print(sqrt(comp_sqrt()))

            case "0":
                break

            case _:
                print("Enter number from 0 to 6, please")

def comp():
    lst = []
    x = float(input("Enter first number to create first complex number: "))
    y = float(input("Enter second numbers to create first complex number: "))
    z = float(input("Enter two numbers to create second complex number: "))
    w = float(input("Enter second numbers to create second complex number: "))
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    print (lst)
    return lst

def comp_sqrt():
    x = float(input("Enter first number to create complex number: "))
    y = float(input("Enter second numbers to create complex number: "))
    a = complex(x, y)
    print(a)
    return a

def rat():
    lst = []
    a = input("Enter first number: ")
    if test(a): lst.append(a)
    b = lst.append(input("Enter second number: "))
    return lst

def rat_sqrt():
    a = float(input("Enter number: "))
    return a
