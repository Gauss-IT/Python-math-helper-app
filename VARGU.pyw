from tkinter import *
from fractions import Fraction
class INTERFACE:
    def __init__(self,master):
        # Dritarja
        self.master = master
        master.title('Seria Dhe Vargu')
        # Inicilizimi
        self.li = []
        self.Hyrja_ = Entry(width=50)
        self.FormuTTT = Label(text="Formula  :")
        self.Kalkulo = Button(text='Kalkulo',command=self.Cal)
        self.GjatsTTT = Label(text="Gjatsia  :")
        self.Hyra2 = Entry(width= 50)
        # Paraqitja e Programit
        self.Hyrja_.grid(row=0,column=1)
        self.FormuTTT.grid(row=0,column=0)
        self.Kalkulo.grid(row=2,column=1)
        self.GjatsTTT.grid(row=1,column=0)
        self.Hyra2.grid(row=1,column=1)
        self.TEXT = Label(text="Vargu 2.1 ± ",font=("Constantia",32))
        self.TEXT.grid(row=2,column=2)
        self.VIJA = (Label(text="Rezultatet")).grid(row=2,column=0)

    def Cal(self):
        li = []
        def Cango(a,b,c=1):
            for i in range(a,b,c):
                t = eval((self.Hyrja_.get()))
                if type(t) == type(1.42):
                    g = Fraction(t).limit_denominator(100)
                    li.append(g)
                    continue

                li.append(t)
        p = list(map(int,(self.Hyra2.get()).split('-')))
        if len(p) == 2 and p[0] > p[1]:
            a = p[0]
            b = p[1]-1
            c = -1
        if len(p) == 2 and p[0] < p[1]:
            a = p[0]
            b = p[1]+1
            c = 1
        if len(p)== 1 and p[0] > 0:
            a = 1
            b = p[0]+1
            c=1
        Cango(a,b,c)
        txt = ' ,'.join(str(a) for a in li)
        b = sum(li)
        Fraction(b).limit_denominator(100)
        c = str(b)
        #Create Output

        self.Vargu = (Label(text='Vargu:')).grid(row=3,column=0)
        self.Texti = (Listbox(width = 50, height = 1 ))
        self.Scr = Scrollbar(orient=HORIZONTAL)
        self.Scr.config(command=self.Texti.xview)
        self.Scr.grid(row=4,column=1,sticky=EW)
        self.Texti.config(xscrollcommand=self.Scr.set)
        self.Texti.insert(END,txt)
        self.Texti.grid(row=3,column=1)
        self.SeraTTT = Label(text="Seria:")
        self.SeraTTT.grid(row=5,column=0)
        self.VLERA = Listbox(width=50,height=1)
        self.VLERA.insert(END,c)
        self.VLERA.grid(row=5,column=1)

root = Tk()
root.geometry('620x190')
root.iconbitmap(r'C:\Users\Vali\Downloads\logomakr_2nl4mo_NBJ_icon.ico')
GUI = INTERFACE(root)
root.mainloop()
