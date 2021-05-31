from tkinter import Button, Canvas, Frame, BOTH
from tkinter.font import names

mem_size = 2800


class Drawer_Window(Frame):

    def __init__(self, memory_size):
        super().__init__()
        self.ProcessColor = "#F69090"
        self.HoleColor = "#90DCF6"
        self.OldProcessColor = "#C090F6"
        self.memory_size = memory_size
        self.initUI()

    # Draw Rectangle into canvas
    def Rect(self, y0, y1, details):

        scale = 480.0 / self.memory_size
        # Creating new y0, y1 variables that has real coordinates
        new_y0 = (y0 + 100)*scale
        new_y1 = y1*scale
        self.canvas.create_rectangle(55, new_y0, 145, new_y1,
                                     outline=details["color"], fill=details["color"])
        # self.canvas.create_rectangle(55, new_y0, 145, new_y1,
        #                              outline=self.HoleColor, fill=self.HoleColor)
        self.canvas.create_text(55-15, new_y0, text=y0)
        self.canvas.create_text(55-15, new_y1, text=y1)
        self.canvas.create_text((55+145) / 2, (new_y0 + new_y1) / 2,
                                text=details["name"], font="bold 8 italic")

    # Color_Guide Rectangles
    def Guide_Rect(self, x0, y0, x1, y1, color, innerText):
        self.canvas.create_rectangle(x0, y0, x1, y1,
                                     outline=color, fill=color)
        # self.canvas.create_text(x0-5, y0, text='0')
        self.canvas.create_text((x1 + x0) / 2, (y1 + y0) / 2,
                                text=innerText, font="bold 8 italic")

    def draw(self, Drawing_List):
        # each element in Drawing_List is tuple (start, end, color)
        for element in Drawing_List:
            y0, y1, details = element
            self.Rect(y0, y1, details)

        self.canvas.mainloop()

    def delete_window(self):
        self.master.quit()
        self.canvas.quit()

    def initUI(self):

        self.master.title("Process Visualization")

        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self, width=400, height=500)

        # # Drawing Main Memmory
        self.Rect(0, self.memory_size-1, {"color": "#C090F6", "name": ""})

        # Creating Guide Rectangles
        self.canvas.create_text(310, 20, text="Guide", font="bold 16")
        self.Guide_Rect(250, 40, 370, 80, self.ProcessColor, "Process")
        self.Guide_Rect(250, 80, 370, 120, self.HoleColor, "Hole")
        self.Guide_Rect(250, 120, 370, 160,
                        self.OldProcessColor, "Old Process")

        self.canvas.pack(fill=BOTH, expand=1)


# ls = [(80, 120, "blue"),
#       (450, 800, "blue"), (1200, 2500, "black")]
# # ls = [(0, 480, "red"), (60, 80, "green")]
# # ls = [(0, 2800, "red")]

# drawer = Drawer_Window(2800)
# # drawer.MemRect(0,2000,"black")
# drawer.draw(ls)
