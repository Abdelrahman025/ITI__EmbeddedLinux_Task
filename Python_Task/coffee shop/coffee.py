from pyfiglet import Figlet
from datetime import datetime
import csv
import os
import time
name = Figlet(font="standard", width=80)
menu_test = Figlet(font="starwars", width=100)
data = "data.csv"
hed = ["type", "cost"]
list_menu_Des = {"Cheesecakes": 50, "Donuts": 25,
                 "Cinnamon rolls": 20, "Tiramisu": 30, "Cakes": 15}
list_menu_coffe = {"Late": 35, "Mocca": 40, "turkey_coffee": 20,
                   "Doppio": 30, "Espresso_one_shot": 25, "Espresso_duble_shot": 40}

with open(data, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(hed)
    writer.writerow(list_menu_Des.keys())
    writer.writerow(list_menu_Des.values())

list_owner_coffe = {}
list_owner_Des = {}
tim = datetime.now()
Item = []
Qty = []
price = []
Subtotal = 0
vat = 0.0
finsh = 1
# while finsh:
os.system('cls')
time.sleep(0.3)
print("\nPlease slecte your chose  ")
choese = input(
    "for customar menu enter 1 : \n""for owner enter 2 : \n")
os.system('cls')
time.sleep(0.3)
while choese == '1':
    # format of text
    # starwars/standard/xsbookb
    print("_ _"*21)
    print(name.renderText("Wellcom In My"))
    print(name.renderText("_Coffee Shop_"))
    print("_ _"*21)
    menu = input("\nfor menu enter 1 : \n""to return back enter 0 : \n")
    if menu == '1':
        print(menu_test.renderText("|_-Menu-_|"))
        print("\n Coffe")
        print("_"*15, "\n")
        for i in list_menu_coffe:
            print(i, "."*10, list_menu_coffe[i])
        print(" "*40, "Desserts")
        print(" "*40, "_"*15, "\n")
        for j in list_menu_Des:
            print(" "*40, j, "."*10, list_menu_Des[j])
    while (menu == '1'):
        print("\nplease choeas what you want for Cof(c) / for Des(d) ....")
        se = input()
        lab = input("enter what you want ")
        num = int(input("enter nmber = "))
        if (se == 'c'):
            Qty.append(num)
            Item.append(lab)
            price.append(list_menu_coffe[lab]*num)
            if lab in list_owner_coffe:
                list_owner_coffe[lab] += num
            else:
                list_owner_coffe.update({lab: num})
        elif (se == 'd'):
            Qty.append(num)
            Item.append(lab)
            price.append(list_menu_Des[lab]*num)
            if lab in list_owner_Des:
                list_owner_Des[lab] += num
            else:
                list_owner_Des.update({lab: num})
        ch = input("if you want some thing else or not (y/n) ")
        if (ch == 'n'):
            # for print total Items
            print(" "*5, "_"*10, "\n")
            print(" "*7, "Coffe")
            print(" "*5, "_"*10, "\n")
            print("print at ", tim.strftime("%Y-%m-%d  %H:%M:%S %p"))
            print("-"*50)
            print("Qry", " "*3, "item", " "*10, "pritce")
            print("-"*50)
            for i in range(len(Qty)):
                Subtotal += price[i]
                print(" ", Qty[i], " "*3, Item[i],
                      " "*11, "EGP", price[i], "\n")
            print("-"*50)
            print("  Subtotal", " "*15, "EGP", Subtotal)
            vat = (Subtotal*14.0)/100
            print("  VAT(14.0%)", " "*13, "EGP", vat)
            print("-"*50)
            print("  Total", " "*18, "EGP", vat+Subtotal)
            Item.clear()
            Qty.clear()
            price.clear()
            i = input()
            if (i == '1'):
                break
    if menu == '0':
        break
while choese == '2':
    x = input(
        "for append to menu enter 1 \nto show sale on day enter 2\nto return back 0")
    if x == '1':
        while 1:
            ple = input(
                "please enter what list you want append to for coffe list (c) / for Des list (d)")
            if (ple == 'c'):
                ap = input("enter the name ")
                pr = int(input("enter price"))
                list_menu_coffe.update({ap: pr})
            elif (ple == 'd'):
                ap = input("enter the name ")
                pr = int(input("enter price"))
                list_menu_Des.update({ap: pr})
            if (input("if you want add again enter (1) /if no enter (0)") == '0'):
                break
    elif (x == '2'):
        while 1:
            p = input("what you want to show coffe 'c' / Des 'd'")
            if p == 'c':
                print(list_owner_coffe)
            elif p == 'd':
                print(list_owner_Des)
            if (input("if you want show again enter (1) /if no enter (0)") == '0'):
                break
    else:
        break
