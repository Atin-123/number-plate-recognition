from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfilename
from model import detect, open_file
import csv

class App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("860x500")
        self.root.resizable(False, False)
        self.root.title("Number Plate Recognition App")
        self.index()
        
    def gotoSecond(self):
        # self.root.forget()
        self.second()
    
    def selectImg(self):
        self.file = askopenfilename(defaultextension='.jpg', filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
        # self.img = ImageTk.PhotoImage(file = self.file)
        self.img  = Image.open(self.file)#import background image
        self.rs_img = self.img.resize((270, 270))
        self.pic = ImageTk.PhotoImage(self.rs_img)
        self.label2 = Label(self.new_window, image=self.pic)
        self.label2.place(x=90, y=130)
        i, j = open_file(self.file)
        self.res = detect(i,j)
        self.im = Image.fromarray(self.res[0])
        self.rs_img1 = self.im.resize((270,270))#import background image
        self.imgtk = ImageTk.PhotoImage(image=self.rs_img1)
        self.label3 = Label(self.new_window, image=self.imgtk)
        self.label3.place(x=450, y=130)
        self.label4 = Label(self.new_window,text="Number:",font="Times 25 bold")
        self.label4.place(x=230, y=420)
        self.label5=Label(self.new_window,text=self.res[1],font="Times 25 bold")
        self.label5.place(x=450, y=420)
        
    def navbar(self, pos):
        # self.button1=Button(pos,text="Home",width=4,height=1,bg="#9b6419",fg="#ffffff", command=self.index)
        self.button2=Button(pos,text="About",width=5,height=1,bg="#9b6419",fg="#ffffff")
        self.button3=Button(pos,text="Social Connect",width=12,height=1,bg="#9b6419",fg="#ffffff")
        self.button4=Button(pos,text="Feedback",width=8,height=1,bg="#9b6419",fg="#ffffff")
        
        # self.button1.place(x=530,y=20)
        self.button2.place(x=570,y=20)
        self.button3.place(x=617,y=20)
        self.button4.place(x=713,y=20)
        
    def index(self):
        self.image  = Image.open("soft.jpg")#import background image
        self.resized_image = self.image.resize((865, 500))
        self.photo = ImageTk.PhotoImage(self.resized_image)
        self.label1 = Label(image=self.photo)
        self.label1.place(x=0, y=0)
        self.label=Label(self.root,text="Number Plate Recognition",font="Times 25 bold",fg="#a0bb25")
        self.button5=Button(self.root,text="Detect Now",font="Times 17 bold",fg="#ffffff",bg="#2cc7bd",command=self.gotoSecond,width=17,height=4)
        self.button6=Button(self.root,text="Number Plate History",font="Times 17 bold", fg = "#ffffff", bg="#2cc7bd",command=self.third,width=18,height=4)
        self.navbar(self.root)
        
        self.label.place(x=250,y=80)
        self.button5.place(x=140, y=250)
        self.button6.place(x=500,y=250)
   
        
    def second(self):
        self.new_window = Toplevel(self.root)
        self.new_window.geometry("860x500")
        self.new_window.resizable(False, False)
        self.navbar(self.new_window)
        self.button=Button(self.new_window,text="Select Image*",font="Times 10 bold",width=20,height=2,bg="#9b6419",fg="#ffffff", command = self.selectImg)
        self.button.place(x=90,y=60)
    #<-----
    def third(self):
        self.new_window2 = Toplevel(self.root)
        self.new_window2.geometry("400x400")
        self.new_window2.resizable(False, False)
        self.frame = Frame(self.new_window2, width=400, height=400)
        self.frame.pack()
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.frame, bg="white", font="verdana 9 bold",width=42, height=27,yscrollcommand=self.scroll.set)
        self.listbox.pack()
        self.filename = "CarNumber.csv"
        fields = []
        rows = []
        
        # reading csv file
        with open(self.filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            
            # extracting field names through first row
            fields = next(csvreader)
        
            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
        
        #  printing  rows
        for row in rows[:]:
            for col in row:
                self.listbox.insert(END,"%10s"%col)
            self.listbox.insert(END, "");
            
    
root = Tk()
obj = App(root)
root.mainloop()