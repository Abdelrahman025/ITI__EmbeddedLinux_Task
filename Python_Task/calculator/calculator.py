choice = int(
    input("enter your choice \n 1- for normal system \n 2- for numeral system \n"))
choice1 = 1            # for normal system
choice2 = 2  # for numeral and binary
while True:
    if (choice == choice1):
        var1 = int(input("enter first digit \n "))
        var2 = int(input("enter second digit\n "))
        operation = int(
            input("enter desired operation \n1-add 2-sub 3-division 4- multi \n"))
        ad = 1
        su = 2
        div = 3
        mult = 4
        if (operation == ad):
            addd = var1+var2  # sum
            print("result of sum= ", +addd)
        elif (operation == su):  # sub
            subb = var1-var2
            print("result of sub =", +subb)
        elif (operation == div):  # division
            divison = var1/var2
            print("result of division =", +divison)
        elif (operation == mult):  # multi
            multi = var1*var2
            print("result of multi =", +multi)
        else:
            print("error")
        again1 = input("to start again enter any key \nto exit enter (no)\n")
        if again1 == "no":
            break

    elif (choice == choice2):
        decimall = int(input("enter value\n"))
        system = int(
            input("choose which system to transfer to 1- binary 2- oct 3- hex \n "))
        bina = 1
        octa = 2
        hexa = 3

        if (system == 1):
            binaa = (bin(decimall))  # to transfer to binary
            print(binaa)
        elif (system == 2):
            octt = (oct(decimall))  # to transfer to octal
            print(octt)
        elif (system == 3):
            hexaa = (hex(decimall))  # to transfer to hexadecimal
            print(hexaa)
        else:
            print("error")
        again2 = input("to start again enter any key  \nto exit enter (no)\n")
        if again2 == "no":
            break

    else:
        print("error")  # if choice not (1 or 2)
        break
