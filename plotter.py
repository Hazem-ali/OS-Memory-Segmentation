from tkinter import Tk, Canvas, Frame, BOTH, font


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    
    def Rect(self, y0, y1, color):
        self.canvas.create_rectangle(55, y0, 145, y1,
                                     outline=color, fill=color)
        self.canvas.create_text(55-5, y0, text=y0)
        self.canvas.create_text(55-5, y1, text=y1)
        

    def Guide_Rect(self, x0, y0, x1, y1, color, innerText):
        self.canvas.create_rectangle(x0, y0, x1, y1,
                                     outline=color, fill=color)
        # self.canvas.create_text(x0-5, y0, text='0')
        self.canvas.create_text((x1+x0) / 2, (y1+y0) / 2,
                                text=innerText, font="bold 11 italic")
        
    

    def initUI(self):

        self.master.title("Process Visualization")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        
        # Creating Guide Rectangles
        self.canvas.create_text(310, 20, text="Guide", font="bold 16")
        self.Guide_Rect(250, 40, 370, 80, "#F69090", "Process")
        self.Guide_Rect(250, 80, 370, 120, "#90DCF6", "Hole")
        self.Guide_Rect(250, 120, 370, 160, "#C090F6", "Old Process")
        
        self.canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex=Example()
    ex.Rect(20, 480, "#90DCF6")
    root.geometry("400x500")
    root.mainloop()
    

if __name__ == '__main__':
    main()
