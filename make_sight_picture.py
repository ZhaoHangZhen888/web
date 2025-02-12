from PIL import Image
import tkinter as tk

class sight_picture:
    def __init__(self):
        self.img = Image.open(get_screen_resolution())
    
    def get_screen_resolution(self):
        root = tk.Tk()
        # 获取屏幕的宽度（单位：像素）
        screen_width = root.winfo_screenwidth()
        # 获取屏幕的高度（单位：像素）
        screen_height = root.winfo_screenheight()
        root.destroy()
        if round(screen_width / screen_height) == round(16/9):
            return '16_9.png'
        else:
            return '4_3.png'

    def make_sight_picture(self):
        pass