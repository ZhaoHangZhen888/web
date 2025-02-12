import math

class mods:
    # 文件打开
    def input_content(self, content, IP):
        with open(IP, 'w') as f:
            f.write(content)

    # 立体图形
    def box(self, x_start, y_start, z_start, x_end, y_end, z_end, resolution=5, slant_angle_x=0, slant_angle_y=0):# 正方体
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
                        content = content + str(-z + z_start)
                    else:
                        content = content + str(z + z_start)
        with open('pixel.txt', 'r') as f:
            content = content + '\n' + f.read()
            if len(f.read()) == 0:
                content = content[1:]
        return content

    def cylinder(self, x, y, z, r, h, resolution=5, slant_angle=90):# 圆柱体
        content = ''
        for hg in range(round(h / resolution) + 1):
            for x_ in range(-r, r + 1):
                for z_ in range(-r, r + 1):
                    dist = (x_ - x) ** 2 + (z_ - y) ** 2
                    if dist <= r ** 2:
                        # 计算倾斜后的高度
                        slanted_h = hg * resolution - h + x_ * math.tan(math.radians(slant_angle))
                        content += f'\n{x_},{slanted_h},{z_}'
        with open('pixel.txt', 'r') as f:
            existing_content = f.read().strip()
        if existing_content:
            content = existing_content + '\n' + content
        return content

    def sphere(self, x, y, z, r, resolution = 5):# 圆球
        content = ''
        content_1 = self.cylinder(x, y-r, z, r, r*2)
        content_2 = self.cylinder(x, y, z-r, r, r*2, slant_angle=0, resolution=resolution)
        content_1_list = content_1.split('\n')
        content_2_list = content_2.split('\n')
        for i in content_1_list:
            if i in content_2_list:
                content = content + i 
        return content

    # 建造
    def make_box(self, x_start, y_start, z_start, x_end, y_end, z_end, resolution=5, slant_angle_x=0, slant_angle_y=0):# 正方体
        content = self.box(x_start, y_start, z_start, x_end, y_end, z_end, resolution, slant_angle_x, slant_angle_y)
        self.input_content(content, 'pixel.txt')

    def make_cylinder(self, x, y, z, r, h, resolution=5, slant_angle=0):# 圆柱体
        content = self.cylinder(x, y, z, r, h, resolution, slant_angle)
        self.input_content(content, 'pixel.txt')


    def make_sphere(self, x, y, z, r):# 圆球
        content = self.sphere(x, y, z, r)
        self.input_content(content, 'pixel.txt')

    # 删除
    def pop(self, content):
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
        self.pop(self.box(x_start, y_start, z_start, x_end, y_end, z_end, resolution, slant_angle_x, slant_angle_y))

    def pop_cylinder(self, x, y, z, r, h, resolution=5, slant_angle=90):# 圆柱体
        self.pop(self.cylinder(x, y, z, r, h, resolution, slant_angle))

    def pop_sphere(self, x, y, z, r, resolution = 5):# 圆球
        self.pop(self.sphere(x, y, z, r, resolution=resolution))