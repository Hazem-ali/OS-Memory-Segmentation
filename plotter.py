from tkinter import Button, Canvas, Frame, BOTH

mem_size = 2800


class Drawer_Window(Frame):

    def __init__(self, memory_size):
        super().__init__()
        self.memory_size = memory_size
        self.initUI()

    def MemRect(self, y0, y1, color):

        self.canvas.create_rectangle(55, 20, 145, 480,
                                     outline=color, fill=color)
        self.canvas.create_text(55-15, 20, text=0)
        self.canvas.create_text(55-15, 480, text=y1)

    def Rect(self, y0, y1, color):

        ratio = 480 / mem_size
        # xy0 = y0 % ratio
        # xy1 = y1 % ratio
        self.canvas.create_rectangle(55, (y0+60)*(480.0/mem_size), 145, y1*(480.0/mem_size),
                                     outline=color, fill=color)
        self.canvas.create_text(55-15, (y0+60)*(480.0/mem_size), text=y0)
        self.canvas.create_text(55-15, y1*(480.0/mem_size), text=y1)

    def Guide_Rect(self, x0, y0, x1, y1, color, innerText):
        self.canvas.create_rectangle(x0, y0, x1, y1,
                                     outline=color, fill=color)
        # self.canvas.create_text(x0-5, y0, text='0')
        self.canvas.create_text((x1+x0) / 2, (y1+y0) / 2,
                                text=innerText, font="bold 11 italic")

    def draw(self, Drawing_List):
        # each element in Drawing_List is tuple (start, end, color)
        for element in Drawing_List:

            self.Rect(element[0], element[1], element[2])

        self.canvas.mainloop()

    def delete_window(self):
        self.master.quit()
        self.canvas.quit()

    def initUI(self):

        self.master.title("Process Visualization")

        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=400, height=500)

        # Drawing Main Memmory
        self.Rect(0, self.memory_size-1, "#C090F6")

        # Creating Guide Rectangles
        self.canvas.create_text(310, 20, text="Guide", font="bold 16")
        self.Guide_Rect(250, 40, 370, 80, "#F69090", "Process")
        self.Guide_Rect(250, 80, 370, 120, "#90DCF6", "Hole")
        self.Guide_Rect(250, 120, 370, 160, "#C090F6", "Old Process")

        self.canvas.pack(fill=BOTH, expand=1)


ls = [ (80, 120, "blue"),
      (450, 800, "blue"), (1200, 2500, "black")]
# ls = [(0, 480, "red"), (60, 80, "green")]
# ls = [(0, 2800, "red")]

drawer = Drawer_Window(2800)
# drawer.MemRect(0,2000,"black")
drawer.draw(ls)

