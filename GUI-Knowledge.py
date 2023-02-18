from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม

B1 = ttk.Button(GUI,text='เงินในบัญชี') #ชื่อปุ่ม
B1.pack(ipadx=20,ipady=20)
B1.place(x=50,y=100)

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('TH SarabunPSK',20),fg=('blue'))
L1.place(x=30,y=20)
######################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showwarning('เงินในบัญชี' ,text)
#showinfo / showerror / showwarning ปุ่มจะมีการแสดงผลและเสียงต่างกัน

FB1 = LabelFrame(GUI,text='Money') #คล้ายกระดาน
FB1.place(x=200,y=70)
B2 = ttk.Button(FB1,text='มีเงินอยู่กี่บาท' ,command=Button2) #ชื่อปุ่ม
B2.pack(ipadx=20,ipady=20,padx=22,pady=22)
#ipad=ขนาดปุ่ม , pad=ขนาดกรอบ

GUI.mainloop()
