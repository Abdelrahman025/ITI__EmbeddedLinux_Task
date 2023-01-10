from tkinter import *
import csv


def viewCost():
    cost = int(smallSizeSpinbox.get()) * 5 + \
        int(mediumSizeSpinbox.get()) * 7 + int(largeSizeSpinbox.get()) * 10
    costLabel.configure(text=str(cost) + " EGP")
    return cost


def purchase():
    data = []
    data.append(smallSizeSpinbox.get())
    data.append(mediumSizeSpinbox.get())
    data.append(largeSizeSpinbox.get())
    data.append(str(viewCost()))

    smallSizeSpinbox.delete(0, 'end')
    mediumSizeSpinbox.delete(0, 'end')
    largeSizeSpinbox.delete(0, 'end')

    smallSizeSpinbox.insert(0, '0')
    mediumSizeSpinbox.insert(0, '0')
    largeSizeSpinbox.insert(0, '0')

    with open("Asab.csv", "a+", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


mainWindow = Tk()

mainWindow.configure(bg='#C3DB79')
mainWindow.title("Asab Shop")
mainWindow.geometry('1000x700')
mainWindow.resizable(0, 0)

welcomeLabel = Label(mainWindow, text="     Welcome to Asab Shop",
                     bd='10', bg='#C3DB79', font=('Calibre', 25, 'bold'))


smallSizeLabel = Label(mainWindow, text="Small",
                       bg='#C3DB79', font=('Calibre', 20, 'bold'))
mediumSizeLabel = Label(mainWindow, text="Medium",
                        bg='#C3DB79', font=('Calibre', 20, 'bold'))
largeSizeLabel = Label(mainWindow, text="Large",
                       bg='#C3DB79', font=('Calibre', 20, 'bold'))

maineSizePhoto = PhotoImage(file='1.png').subsample(2, 2)
maineSizePhotoLabel = Label(mainWindow, image=maineSizePhoto)

smallSizePhoto = PhotoImage(file='4.png').subsample(2, 2)
smallSizePhotoLabel = Label(mainWindow, image=smallSizePhoto)

mediumSizePhoto = PhotoImage(file='3.png').subsample(2, 2)
mediumSizePhotoLabel = Label(mainWindow, image=mediumSizePhoto)

largeSizePhoto = PhotoImage(file='2.png').subsample(3, 3)
largeSizePhotoLabel = Label(mainWindow, image=largeSizePhoto)

smallSizeSpinbox = Spinbox(mainWindow, from_=0, to=10,
                           width=5, font=('Calibre', 15, 'bold'))

mediumSizeSpinbox = Spinbox(
    mainWindow, from_=0, to=10, width=5, font=('Calibre', 15, 'bold'))

largeSizeSpinbox = Spinbox(mainWindow, from_=0, to=10,
                           width=5, font=('Calibre', 15, 'bold'))

viewCostButton = Button(mainWindow, text="View Cost", font=(
    'Calibre', 15, 'bold'), command=viewCost)
purchaseButton = Button(mainWindow, text="Purchase", font=(
    'Calibre', 15, 'bold'), command=purchase)

costLabel = Label(mainWindow, text="0 EGP", font=(
    'Calibre', 15, 'bold'), bg='#C3DB79')

welcomeLabel.place(x=270, y=0)


smallSizeLabel.place(x=157, y=350)
mediumSizeLabel.place(x=447, y=350)
largeSizeLabel.place(x=757, y=350)

maineSizePhotoLabel.place(x=300, y=70)
smallSizePhotoLabel.place(x=140, y=390)
mediumSizePhotoLabel.place(x=450, y=390)
largeSizePhotoLabel.place(x=705, y=390)

smallSizeSpinbox.place(x=165, y=550)
mediumSizeSpinbox.place(x=465, y=550)
largeSizeSpinbox.place(x=765, y=550)

viewCostButton.place(x=390, y=650)
costLabel.place(x=510, y=656)
purchaseButton.place(x=450, y=590)


mainWindow.mainloop()
