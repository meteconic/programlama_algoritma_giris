import tkinter
def hesap():
    a=int(E1.get())
    b=int(E2.get())
    aci=int(E3.get())
    pi=3.14
    import math
    alan=a*b*math.sin(aci*pi/180)/2
    from tkinter import messagebox
    messagebox.showinfo("Üçgenin alanı",alan)
        
root=tkinter.Tk()

etiket1=tkinter.Label(root,text="a kenarının değerini giriniz")
etiket1.grid(row=1,column=0,padx=110,pady=10)

etiket2=tkinter.Label(root,text="b kenarını giriniz")
etiket2.grid(row=2,column=0,padx=110,pady=10)

etiket3=tkinter.Label(root,text="İkisinin arasındaki açının değerini giriniz")
etiket3.grid(row=3,column=0,padx=110,pady=10)

E1=tkinter.Entry(root,bd=2)
E1.grid(row=3,column=1,padx=110,pady=3)

E2=tkinter.Entry(root,bd=2)
E2.grid(row=2,column=1,padx=110,pady=3)

E3=tkinter.Entry(root,bd=2)
E3.grid(row=1,column=1,padx=110,pady=3)

button1=tkinter.Button(root,text="Hesapla",width=20,command=hesap)
button1.grid(padx=110,pady=70)
