import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import tkintermapview as tkmap
from PIL import Image,ImageTk

class MyCustomDialog(Dialog):
    def __init__(self, parent, record:list, title = None):
       print('HI mycustomdialog')
       print(f'傳過來的record:{record}')
       self.date = record[0]
       self.county = record[1]
       self.sitename = record[2]
       self.aqi = record[3]
       self.pm25 = record[4]
       self.status = record[5]
       self.lat = float(record[6])
       self.lon = float(record[7])
       super().__init__(parent = parent, title = title) 

    def body(self,master):
        # tk.Label(master,text='輸入名字').grid(row=0)
        # self.name_entry = tk.Entry(master)
        # self.name_entry.grid(row=0,column=1)
        # return self.name_entry #focus到input框
        main_frame = ttk.Frame(master,borderwidth=1,relief='groove')
        ttk.Label(main_frame, text=self.date,font = ("Helvetica",24,"bold")).pack(pady=20)
        #-------------------------------------------------------
        canvas_left = tk.Canvas(main_frame,width=200,height=200)

        if self.aqi <=50:
            path = './image/green.png'
            self.status = '良好'
        elif self.aqi <=100:
            path = './image/yellow.png'
            self.status = '普通'
        else:
            path = './image/red.png'
            self.status = '暖心之都'

        canvas_left.create_rectangle(10,10,190,190,outline="#808080",width=2)
        canvas_left.create_text(100,40,text=f'AQI:{self.status}', font=("Helvetica",24,"bold"), fill='#9E7A7A')

        self.leftimg = ImageTk.PhotoImage(Image.open(path))
        canvas_left.create_text(100,160,text=f'AQI:{self.aqi}', font=("Helvetica",24,"bold"), fill='#9E7A7A')
        canvas_left.create_image(100,100,anchor = 'center', image = self.leftimg)
        canvas_left.pack(side='left')
        #-------------------------------------------------------
        canvas_right = tk.Canvas(main_frame,width=200,height=200)

        if self.pm25 <=15.4:
            path = './image/green.png'
            self.pm25_status = '良好'
        elif self.pm25 <=35.4:
            path = './image/yellow.png'
            self.pm25_status = '普通'
        else:
            path = './image/red.png'
            self.pm25_status = '危險'

        canvas_right.create_rectangle(10,10,190,190,outline="#808080",width=2)
        canvas_right.create_text(100,40,text=f'pm25:{self.pm25_status}', font=("Helvetica",24,"bold"), fill='#9E7A7A')

        self.rightimg = ImageTk.PhotoImage(Image.open(path))
        canvas_right.create_image(100,100,anchor = 'center', image = self.rightimg)
        canvas_right.create_text(100,160,text=f'PM2.5:{self.pm25}', font=("Helvetica",24,"bold"), fill='#9E7A7A')
        canvas_right.pack(side='right')
        #-------------------------------------------------------
        main_frame.pack(expand=True,fill='x')
        #-------------------------------------------------------
        map_frame = ttk.Frame(master)
        map_widget = tkmap.TkinterMapView(map_frame,
                                         width=400,
                                         height=400,
                                         corner_radius=0
                                         )
        map_widget.set_position(self.lat,self.lon,marker=True)
        map_widget.pack()
        map_frame.pack(padx=10,pady=10)

    def apply(self):
        print('使用者按了apply')

    def buttonbox(self):
        box = tk.Frame(self)
        self.ok_button = tk.Button(box,text='OK',width=10,command = self.ok,default = tk.ACTIVE)
        self.ok_button.pack(side = tk.LEFT,padx=5, pady=5)
        self.cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>",self.ok)
        self.bind("<Escape>",self.cancel)
        box.pack()

    def ok(self,event = None):
        print('OK被按了')
        super().ok()

    def cancel(self, event = None):
        print('Cancel被按了')
        super().cancel()
