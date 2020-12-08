from tkinter import *
from random import choice
from PIL import Image, ImageTk


root = Tk()
root.geometry("400x400")
root.title("Dice Rolling Simulator")
root.iconbitmap("icon/dice.ico")
root.configure(background = "purple1")


class app(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand = True)
        self.start_frame = None
        self.dice_frame = None
        self.start()


    def start(self):
        if self.dice_frame:
            self.dice_frame.pack_forget()

        if self.start_frame:
            self.start_frame.pack(expand = True)

        else:
            button_frame = self.start_frame = Frame(self)
            button_frame.pack(expand = True)

            Button(button_frame, text = "Start", font = ("Helvetica", 12), fg = "blue", command = self.dice, height = 3, width = 15).pack(expand = True)


    def dice(self):
        if self.start_frame:
            self.start_frame.pack_forget()

        if self.dice_frame:
            self.dice_frame.pack(expand = True)

        else:
            button_frame = self.dice_frame = Frame(self)
            button_frame.pack(expand = True)

            dice = ["dice image/1.jpg", "dice image/2.jpg", "dice image/3.jpg", "dice image/4.jpg", "dice image/5.jpg", "dice image/6.jpg"]
            dice_img = ImageTk.PhotoImage(Image.open(choice(dice)))
            img_label = Label(app, image = dice_img)
            img_label.image = dice_img
            img_label.pack(expand = True)


            def rolling_dice():
                dice_img = ImageTk.PhotoImage(Image.open(choice(dice)))
                img_label.configure(image = dice_img)
                img_label.image = dice_img


            Button(button_frame, text = "Roll the Dice", font = ("Helvetica", 10), bg = "black", fg = "white", command = rolling_dice, height = 2, width = 24).pack(expand = True)
            Button(button_frame, text = "Exit", font = ("Helvetica", 10), bg = "light grey", fg = "black", command=root.destroy, height = 2, width = 18).pack(expand = True)


app = app(root)
root.mainloop()

