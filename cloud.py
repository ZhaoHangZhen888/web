class cloud:
    def cloud_variables(self, s):
        # 使用绝对路径来确保文件可以被正确找到
        with open('云端.txt', 'r', encoding="utf-8") as f:
            content = f.read()
        content = content + '\n' + s
        with open('云端.txt', 'w', encoding="utf-8") as f:
            f.write(content)