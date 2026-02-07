from tkinter.ttk import Progressbar
from tkinter.ttk import Style
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk,Image
import os.path as pth
from threading import Thread



class StartScreen(Tk):
    def __init__(self,windo_wdth=427,window_height=250, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        print('STARTING')
        # self.wm_attributes('-transparent', True)
        # self.config(bg='systemTransparent')
        self.thr = ''
        self.width_of_window = windo_wdth
        self.height_of_window = window_height
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        s = Style()
        s.theme_use('clam')
        s.configure('red.Horizontal.TProgressbar', foreground='red', background='gold' , font=('calibri', 16, 'bold'))
        self.root_window()
        Frame(self, width=self.width_of_window, height=self.height_of_window, bg='systemTransparent').place(x=0, y=0)
        self.bg_img()

        self.progress = Progressbar(self, style='red.Horizontal.TProgressbar', orient=HORIZONTAL,
                                    length=self.width_of_window*0.95,
                                    mode="determinate")
        b1 = Button(self, width=15, height=2, text='GET STARTED', font=('calibri', 24, 'bold'), command=self.bar, border=0, fg='goldenrod', activebackground='skyblue3')
        b1.place(x=100, y=self.height_of_window*0.65)
        b2 = Button(self, width=2, height=1, text='X', font=('calibri', 24, 'bold'), command=self.colse_w, border=0, fg='goldenrod', activebackground='skyblue3')
        b2.place(x=self.width_of_window-50, y=10)

        self.progress.place(x=-10, y=self.height_of_window * 0.80)
        self.title()
        self.title2()
        self.slogan()


    def colse_w(self):
        self.destroy()

    def root_window(self):
        width_of_window = self.width_of_window
        height_of_window = self.height_of_window
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # screen_width = 1280
        # screen_height = 720
        x_coordinate = int((screen_width / 2) - (width_of_window / 2))
        y_coordinae = int((screen_height / 2) - (height_of_window / 2))
        # w.geometry('200x150+400+300')
        self.geometry(f'{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinae}')
        self.overrideredirect(1)
        self.overrideredirect(0)

    def main_window(self, v=True):
        q = Tk()
        width_of_window = self.width_of_window
        height_of_window = self.height_of_window
        screen_width = q.winfo_screenwidth()
        screen_height = q.winfo_screenheight()
        # screen_width = 1280
        # screen_height = 720
        x_coordinate = int((screen_width / 2) - (width_of_window / 2))
        y_coordinae = int((screen_height / 2) - (height_of_window / 2))
        q.geometry(f'{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinae}')
        l1 = Label(q, text='AD Text Here..', fg='dark grey', bg=None)
        fo1 = ('Calirbi (Body)', 24, 'bold')
        l1.config(font=fo1)
        l1.place(x=88, y=100)
        if v:
            pass
        else:
            pass
            # q.overrideredirect(1)
        q.withdraw()
        filename = askopenfilename()
        q.mainloop()

    def title(self, title='MTM Pharmacy', y=0.45):
        x = 10
        self.tit_x = len(title) * 22.5 + x
        self.tit_y = self.height_of_window*y
        print(f' X FACTOR >>>>>::{self.tit_x}')
        l1 = Label(self, text=title, fg='white', bg='#249794')
        fon1 = ('Calibri (Body)', 32, 'bold')
        l1.config(font=fon1)
        l1.place(x=x, y=self.tit_y)

    def title2(self, title2='SCREEN'):
        l2 = Label(self, text=title2, fg='white', bg='skyblue3')
        fo2 = ('Calibri (Body)', 24)
        l2.config(font=fo2)
        l2.place(x=self.tit_x, y=self.tit_y+2)

    def slogan(self, slogan='Together is Better'):
        l3 = Label(self, text=slogan, fg='white', bg='skyblue3')
        fo3 = ('Calibri (Body)', 13)
        l3.config(font=fo3)
        l3.place(x=45, y=self.tit_y+50)

    def logo(self, img_name='points_logo-01.png'):
        print(img_name)
        img_n = img_name
        img_f = pth.join('data', img_n)
        print(img_f)
        self.img = ImageTk.PhotoImage(Image.open(img_f).resize((120, 100),Image.ANTIALIAS))
        panel = Label(self, image=self.img)
        panel.config(bg='systemTransparent')
        panel.img = self.img
        panel.place(x=self.width_of_window * 0.90, y=f'{(self.height_of_window / 2) - (self.img.height() / 2)}')

    def bg_img(self, img_name='start.png'):
        print(img_name)
        img_n = img_name
        img_f = pth.join('data', img_n)
        print(img_f)
        # Load image with alpha
        img = Image.open(img_f).convert('RGBA')
        img = img.resize((self.width_of_window, self.height_of_window), Image.Resampling.LANCZOS)
        self.img_bg = ImageTk.PhotoImage(img)
        # Use Canvas for proper transparency
        self.bg_canvas = Canvas(self, width=self.width_of_window, height=self.height_of_window, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0)
        # self.bg_canvas.config(bg='systemTransparent')
        self.bg_canvas.create_image(0, 0, anchor='nw', image=self.img_bg)
        
        # # self.img_bg = ImageTk.PhotoImage(Image.open(img_f).resize((self.width_of_window, self.height_of_window), Image.ANTIALIAS))
        # self.img_bg = ImageTk.PhotoImage(
        #     Image.open(img_f).resize((self.width_of_window, self.height_of_window), Image.Resampling.LANCZOS))
        # # Keep a reference to the label to prevent garbage collection
        # if hasattr(self, 'bg_label'):
        #     self.bg_label.config(image=self.img_bg)
        # else:
        #     self.bg_label = Label(self, image=self.img_bg, bg='systemTransparent')  # use a real bg color
        #     self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # panel = Label(self, image=self.img_bg)
        # panel.config(bg='systemTransparent')
        # panel.img = self.img_bg
        # panel.place(x=0, y=0)
        

    def progress(self, style='red.Horizontal.TProgressbar', length=500, f_color='red', b_color='red'):
        s = Style()
        s.theme_use('clam')
        s.configure(style, foreground=f_color, background=b_color)
        progress = Progressbar(self, style=style, orient=HORIZONTAL, length=length,
                               mode="determinate")
        progress.place(x=-10, y=235)
        return progress

    def bar_start(self):
        l4 = Label(self, text='Loading....', fg='white', bg='#249794')
        font2 = ('Calibri (Body)', 18)
        l4.config(font=font2)
        l4.place(x=0, y=self.height_of_window * 0.70)
        # self.withdraw()


    def bar(self):
        print('BAR>>>>>')
        # self.after(100)
        # t1 = Thread(target=self.thr)
        # t1.start()
        print("bar In Progress...")
        r = 0
        for i in range(50):
            # print('.')
            self.progress['value'] = r
            self.update_idletasks()
            self.after(30)
            r += 1
        self.withdraw()
        self.after(30)
        self.thr()
        # self.destroy()
        # self.withdraw()
        # self.after(30)
        print('Waiting Eel')
        # t1.join()
        # self.after(30)
        # self.destroy()
        # self.main_window()
        # print('THreadd: ', t1.isAlive())
        print('ELL FINISH NOw In TK')


    def select_file(self):
        print('FILE FROM ')
        # self.after(30, self.deiconify())
        # q = Tk()
        # q.wm_attributes('-topmost', 1)
        # q.withdraw()
        # lift_window(self, self)
        # self.after(30)
        # q.withdraw()
        filename = askopenfilename()
        # self.after(30, self.deiconify())
        # self.wm_attributes('-topmost', 0)
        # print(filename)
        return filename

#
# def lift_window(win):
#     win.lift()
#     win.after(1000, lift_window)


def thr_():
    print('ANY THING........>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(100):
        print('ANY THING........>>>>>>>>>>>>>>>>>>>>>>>>')


def start():
    app = StartScreen()
    app.mainloop()


def select_file_():
    # from tkinter import Tk
    # from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    filename = askopenfilename()
    # print(filename)
    return filename


if __name__ == '__main__':

    x = StartScreen(624, 400)
    x.title('MTM PHARMACY')
    x.thr = thr_()
    x.wm_attributes('-transparent', True)
    x.config(bg='systemTransparent')
    x.mainloop()
    print()

