import math
from PIL import Image
import tkinter as tk

class mods:
    # 文件打开
    def input_content(self, content, IP):
        with open(IP, 'w') as f:
            f.write(content)

    # 立体图形
    def box(self, x_start, y_start, z_start, x_end, y_end, z_end, color=(255,255,255), resolution=5, slant_angle_x=0, slant_angle_y=0):# 正方体
        center_x = (x_start + x_end) / 2
        center_y = (y_start + y_end) / 2
        center_z = (z_start + z_end) / 2
        content = ''
        for x in range(round(abs((x_end - x_start) / resolution))):
            for y in range(round(abs((y_end - y_start) / resolution))):
                for z in range(round(abs((z_end - z_start) / resolution))):
                    offset_x = x - center_x
                    offset_y = y - center_y
                    offset_z = z - center_z
                    # 使用三角函数计算倾斜后的 x 和 y 坐标
                    x_tilted = offset_x * math.cos(math.radians(slant_angle_x)) - offset_y * math.sin(math.radians(slant_angle_x))
                    y_tilted = offset_x * math.sin(math.radians(slant_angle_y)) + offset_y * math.cos(math.radians(slant_angle_y))
                    x_abs = x_tilted + center_x
                    y_abs = y_tilted + center_y
                    if x_end < x_start:
                        content = content + '\n' + str(-x_abs + x_start) + ','
                    else:
                        content = content + '\n' + str(x_abs + x_start) + ','
                    if y_end < y_start:
                        content = content + str(-y_abs + y_start) + ','
                    else:
                        content = content + str(y_abs + y_start) + ','
                    if z_end < z_start:
                        content = content + str(-z + z_start) + ','
                    else:
                        content = content + str(z + z_start) + ','
        content = content + color
        with open('pixel.txt', 'r') as f:
            content = content + '\n' + f.read()
            if len(f.read()) == 0:
                content = content[1:]
        return content
        

    def cylinder(self, x, y, z, r, h, collor, resolution=5, slant_angle=90):# 圆柱体
        content = ''
        for hg in range(round(h / resolution) + 1):
            for x_ in range(-r, r + 1):
                for z_ in range(-r, r + 1):
                    dist = (x_ - x) ** 2 + (z_ - y) ** 2
                    if dist <= r ** 2:
                        # 计算倾斜后的高度
                        slanted_h = hg * resolution - h + x_ * math.tan(math.radians(slant_angle))
                        content += f'\n{x_},{slanted_h},{z_}'
        content = content + color
        with open('pixel.txt', 'r') as f:
            existing_content = f.read().strip()
        if existing_content:
            content = existing_content + '\n' + content
        return content

    def sphere(self, x, y, z, r,color, resolution = 5):# 圆球
        content = ''
        content_1 = self.cylinder(x, y-r, z, r, r*2, color, resolution=resolution)
        content_2 = self.cylinder(x, y, z-r, r, r*2, color, slant_angle=0, resolution=resolution)
        content_1_list = content_1.split('\n')
        content_2_list = content_2.split('\n')
        for i in content_1_list:
            if j in content_2_list:
                content = content + i 
        with open('pixel.txt', 'r') as f:
            content = f.read() + content
        return content

    # 建造
    def make_box(self, x_start, y_start, z_start, x_end, y_end, z_end, color, resolution=5, slant_angle_x=0, slant_angle_y=0):# 正方体
        content = self.box(x_start, y_start, z_start, x_end, y_end, z_end, color, resolution=resolution, slant_angle_x=slant_angle_x, slant_angle_y=slant_angle_y)
        self.input_content(content, 'pixel.txt')

    def make_cylinder(self, x, y, z, r, h, color, resolution=5, slant_angle=0):# 圆柱体
        content = self.cylinder(x, y, z, r, h, color, resolution=resolution, slant_angle=slant_angle)
        self.input_content(content, 'pixel.txt')


    def make_sphere(self, x, y, z, r,color, resolution = 5):# 圆球
        content = self.sphere(x, y, z, r, color, resolution=resolution)
        self.input_content(content, 'pixel.txt')

    # 删除
    def pop(self, content):# 删除统一代码
        content = content.split('\n')
        for i in content:
            with open('pixel.txt', 'r') as f:
                linds = f.readlines()
                linds_input = ''
                for j in range(len(linds)):
                    linds[j] = linds[j][:len(linds[j])]
                for j in range(len(linds)):
                    if int(i[0]) - int(linds[j].split(',')[0]) < resolution and int(i[1]) - int(linds[j].split(',')[1]) < resolution and int(i[2]) - int(linds[j].split(',')[2]) < resolution:
                        pass
                    else:
                        linds_input = linds_input + linds[j]
                self.input_content(linds_input, 'pixel.txt')

    def pop_box(self, x_start, y_start, z_start, x_end, y_end, z_end, resolution=5, slant_angle_x=0, slant_angle_y=0):# 圆柱
        self.pop(self.box(x_start, y_start, z_start, x_end, y_end, z_end, resolution=resolution, slant_angle_x=slant_angle_x, slant_angle_y=slant_angle_y))

    def pop_cylinder(self, x, y, z, r, h, resolution=5, slant_angle=90):# 圆柱体
        self.pop(self.cylinder(x, y, z, r, h, resolution, slant_angle))

    def pop_sphere(self, x, y, z, r, resolution = 5):# 圆球
        self.pop(self.sphere(x, y, z, r, resolution=resolution))


class sight_picture:
    def __init__(self):
        # 打开图片
        self.img = Image.open(self.choose_image_according_to_resolution_size())
        silf.img_size = self.img.size
        
    def get_screen_resolution(self):
        root = tk.Tk()
        # 获取屏幕的宽度（单位：像素）
        screen_width = root.winfo_screenwidth()
        # 获取屏幕的高度（单位：像素）
        screen_height = root.winfo_screenheight()
        root.destroy()
        return screen_width,screen_height

    def choose_image_according_to_resolution_size(self):
        screen_width,screen_height = self.get_screen_resolution()
        if round(screen_width / screen_height) == round(16/9):
            return '16_9.png'
        else:
            return '4_3.png'
            
    def make_sight_picture(self, view, x, y, z, resolution=5, angle_left_right=0, angle_up_down=0):
        """
        初始角度面向x维度线
        view为视角距离
        view的距离等于(view/resolution*100)
        pixel_list[i] [x,y,z,(r,g,b)]
        """
        with open('pixel', 'r') as f:
            pixel_list = f.readline()

        # 选择
        will_pop = []
        for i in range(len(pixel_list)):
            pixel_list[i] = pixel_list[i].split(',')
            pixel_list[i][0] = pixel_list[i][0] - x
            pixel_list[i][1] = pixel_list[i][1] - y
            pixel_list[i][2] = pixel_list[i][2] - z
            # distance = math.sqrt(pixel_list[i][0]**2+pixel_list[i][1]**2+pixel_list[i][2]**2)
            # if distance>view:
            #     will_pop.append(pixel_list[i])
            # else:
            #     pixel_list.append(distance)
            if pixel_list[i][0]-x < view or pixel_list[i][1]-y < view or pixel_list[i][2]-z < view:
                will_pop.append(pixel_list[i])

        # 删除
        for i in will_pop:
            for j in range(len(pixel_list)):
                if pixel_list[j] == i:
                    pixel_list.pop(j)
                    break

        # # 排序
        # image_pixel_list = [pixel_list[-1]]
        # for i in pixel_list[:-1]:
        #     for j in range(image_pixel_list+1):
        #         if i[5]>image_pixel_list[j][5]:
        #             image_pixel_list.insert(j,i)

        # 绘画
        for i in range(math.sqrt(((1-angle_up_down%90/90)*(1-angle_left_right%90/90))**2 + (angle_up_down%90/90)**2 + (angle_up_down%90/90)**2)*(view/resolution*100)//resolution+1, resolution, -resolution):
            if angle_up_down//90<1:
                if angle_left_right//90<1:
                    for j in range(self.img_size[0]/2*view/resolution,-(self.img_size[0]/2*view/resolution),-1):
                        aim_x, aim_y, aim_z = (1-angle_up_down%90/90)*(1-angle_left_right%90/90), (angle_up_down%90/90), (angle_up_down%90/90)
                        for k in pixel_list:
                            if abs(k[0]-aim_x)<=resolution and abs(k[1]-aim_y)<=resolution and abs(k[2]-aim_z)<=resolution:
                                self.img.putpixel()