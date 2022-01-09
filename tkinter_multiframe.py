try:
    import tkinter as tk              
except ImportError:
    import Tkinter as tk   
from tkinter import font as tkfont
from tkinter import PhotoImage
import numpy
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import ImageTk,Image
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

       
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        from PIL import ImageTk,Image
        self.controller = controller
        label = tk.Label(self, text="Home", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Page 1",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Page 2",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Page 3",
                            command=lambda: controller.show_frame("PageThree"))        
        #label2=tk.Label(self,text="Heading", font=("Arial",10))    #add a heading        
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        button1.pack()
        button2.pack()
        button3.pack()
       # label2.pack() #add a heading
    


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Page 2",
                            command=lambda: controller.show_frame("PageTwo"))
        button3 = tk.Button(self, text="Page 3",
                            command=lambda: controller.show_frame("PageThree"))
       # img = ImageTk.PhotoImage(Image.open("")) #add image on screen
        #panel = tk.Label(self, image = img)
       # panel.pack(side = "bottom", fill = "both", expand = "yes")
    
        #panel.pack(side = "bottom", fill = "both", expand = "yes")
        button.pack()
        button2.pack()
        button3.pack()
        #panel.pack(side = "bottom", fill = "both", expand = "yes")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
                           
        button1 = tk.Button(self, text="Page 1",
                            command=lambda: controller.show_frame("PageOne"))
        button3 = tk.Button(self, text="Page 3",
                            command=lambda: controller.show_frame("PageThree"))
        button.pack()
        button1.pack()
        button3.pack()
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("StartPage"))
                           
        button1 = tk.Button(self, text="Page 1",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Page 2",
                            command=lambda: controller.show_frame("PageTwo"))                   
        button.pack()
        button1.pack()
        button2.pack()
        f=Figure(figsize=(5,5), dpi=100)
        a= f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8,5,76,3,34,43,6,2])
        canvas = FigureCanvasTkAgg(f,self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH, expand= True)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

