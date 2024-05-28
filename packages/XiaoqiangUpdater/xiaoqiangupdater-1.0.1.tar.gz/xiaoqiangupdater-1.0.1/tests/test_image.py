# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/28 8:04
# 文件名称： test_image.py
# 项目描述： 测试
# 开发工具： PyCharm
from XiaoqiangUpdater import png_logo, get_image_path, ico_logo
import tkinter as tk
from tkinter import ttk


def app():
    root = tk.Tk()
    root.title("XiaoqiangClub")

    # 设置窗口大小
    root.geometry("400x200")

    # 设置窗口图标
    try:
        root.iconphoto(True, tk.PhotoImage(file=png_logo()))
    except Exception as e:
        print(f"Error loading logo: {e}")

    # 创建标签
    label = ttk.Label(root, text="XiaoqiangClub v1.0.0", font=("Helvetica", 24))
    label.pack(expand=True)

    root.mainloop()


if __name__ == '__main__':
    print(get_image_path('updater_logo.ico'))
    print(get_image_path('updater_logo.png'))
    print(ico_logo())
    print(png_logo())
    app()
