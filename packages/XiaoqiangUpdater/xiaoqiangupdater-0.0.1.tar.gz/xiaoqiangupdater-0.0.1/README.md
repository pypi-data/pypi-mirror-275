<p align="center"><a href="https://github.com/xiaoqiangclub/XiaoqiangUpdater"><img width="200" src="img/logo.png" alt="Project logo"></a></p>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-3115/"><img src="https://img.shields.io/badge/Python-3.11.5-blue" alt="Python version"></a>
  <a href="https://github.com/xiaoqiangclub/updater/blob/master/LICENSE"><img src="https://img.shields.io/github/license/xiaoqiangclub/updater" alt="License"></a>
</p>

# XiaoqiangUpdater

这是一个通用的自动更新模块，适用于Windows项目（因为时间有限，没有测试其他平台）。该模块包括一个独立的更新程序，能够检测、下载和安装更新，并重启主应用程序。

## 实现原理

该模块通过检查当前版本和最新版本之间的差异，从指定的URL下载更新包，并验证其完整性。然后将更新包解压到指定的安装路径，并重启主应用程序。

**使用该模块需要满足以下条件：**

1. 你的项目发布时打包成一个`zip格式`的压缩包。
2. 你的项目需要提供一个`exe入口文件`，用于启动更新程序。
3. 你的项目如果是多目录多文件，exe文件需要在你项目的根目录下。
4. 当你发布新版本的时候，建议保持`exe入口文件名`不变（例如：`app.exe`），否则需要你每次都在`updater_config.json`
   中修改`main_app`字段。

## 技术栈

- Python 3.11.5
- requests
- tkinter
- psutil
- pyinstaller

## 安装

使用 pip 安装：

```sh
pip install XiaoqiangUpdater
```

## 使用说明

### 参数说明

使用更新程序 `updater` 时，可以指定以下参数：

- `config_path`：配置文件路径（默认为 `updater_config.json`
  ，如果没有指定具体的配置文件路径，程序将自动在当前目录下遍历查找一个名叫 `updater_config.json` 的配置文件。）
- `--help`：显示此帮助信息并退出。

### 配置文件说明

示例配置文件 `updater_config.json` 的内容如下：

```json
{
  "current_version": "1.0.0",
  "latest_version": "1.1.0",
  "update_url": "http://example.com/updater.zip",
  "main_app": "app.exe",
  "verify_file_md5": "d41d8cd98f00b204e9800998ecf8427e",
  "logo_path": "path/to/logo.png",
  "open_current_version_on_fail": true,
  "install_dir": "path/to/install/directory"
}
```

#### 配置项说明

- `current_version`：当前版本号。
- `latest_version`：最新版本号。
- `update_url`：更新包的下载URL。
- `main_app`：主程序的路径（相对路径：一般都是放在根目录下的exe入口文件）。
- `verify_file_md5`：更新包校验文件的MD5值（可选），可以直接调用模块中的`get_file_md5`方法获取。
- `logo_path`：图形用户界面的图标路径（可选）。
- `open_current_version_on_fail`：更新失败或取消时是否打开当前版本的程序（可选）。默认是 `True`。
- `install_dir`：软件解压更新的目录（可选）。默认是 `updater.exe` 所在的目录。

**注意：**

1. 模块会自动使用 `updater.exe` 文件所在的目录与设置的相对路径或目录名进行拼接。
2. 如果没有指定具体的配置文件路径，程序将自动在当前目录下遍历查找一个名叫 `updater_config.json` 的配置文件。

#### 生成示例配置文件

- 你可以调用`updater_config_example方法`快速生成一个示例配置文件：

   ```python
   from XiaoqiangUpdater import updater_config_example

   if __name__ == '__main__':
       updater_config_example(save_path='updater_config.json')
   ```

### 打包更新程序

**直接使用**

- 第一种方式可以直接下载打包好的通用exe文件：[最新版下载地址](https://github.com/xiaoqiangclub/XiaoqiangUpdater/releases)

**手动打包**

- 配置updater(可默认)
   ```python
   from XiaoqiangUpdater import (updater, updater_config_example)

   
   def test_updater():
       updater_config_example(save_path='updater_config.json') # 这里为了方便生成一个示例配置文件，这里需要你根据自己的项目去生成
       updater(config_path='updater_config.json')   # 指定配置文件路径，不指定：默认会自动在当前目录下遍历查找名为updater_config.json的配置文件
   
   
   if __name__ == '__main__':
       test_updater()
   ```

- 调用`pack_to_exe`方法，将 `your_updater` 打包成可执行文件：
   ```python
   from XiaoqiangUpdater import pack_to_exe
   
   if __name__ == '__main__':
       pack_to_exe(main_file='test_updater.py', with_cmd_window=False, app_ico_logo=None)
   ```

## 项目中使用示例

```python
# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/25 11:01
# 文件名称： app.py
# 项目描述： 测试程序
# 开发工具： PyCharm
import os
import json
import subprocess
import sys
import tkinter as tk
from tkinter import ttk
from XiaoqiangUpdater import updater, updater_config_example


def app():
    root = tk.Tk()
    root.title("XiaoqiangClub")

    # 设置窗口大小
    root.geometry("400x200")

    # 设置窗口图标
    try:
        root.iconphoto(True, tk.PhotoImage(file="xiaoqiangclub_logo.png"))
    except Exception as e:
        print(f"Error loading logo: {e}")

    # 创建标签
    label = ttk.Label(root, text="XiaoqiangClub v1.0.0", font=("Helvetica", 24))
    label.pack(expand=True)

    root.mainloop()


def generate_config():
    """
    注意：这个函数仅用于生成示例配置文件，在实际使用中需要你自己去写这个函数。
    """
    config_path = os.path.join(os.getcwd(), "updater_config.json")
    updater_config_example(save_path=config_path)
    print(f"配置文件已生成：{config_path}")


# 用于生产环境调用exe文件
def main():
    try:
        # 调用生成配置文件函数
        generate_config()
        # 调用更新程序
        updater_path = os.path.join(os.getcwd(), "updater.exe")
        subprocess.Popen([updater_path])
        sys.exit()
    except Exception as e:
        print(f"检查更新时出错: {e}")


# 仅用于测试，调用updater.py中的start_update函数
def main_test():
    try:
        # 调用生成配置文件函数
        generate_config()
        # 调用更新逻辑
        updater("updater_config.json")
        sys.exit()
    except Exception as e:
        print(f"检查更新时出错: {e}")


if __name__ == "__main__":
    # 生产环境使用：
    # main()

    # 测试使用：
    main_test()
    # 启动应用程序
    app()
```

## 注意事项

- `generate_config`方法需要你自己去写，用于生成配置文件。
- 请确保更新URL和文件路径正确，并且更新包完整。
- 为了确保安全，建议验证下载文件的完整性。
- 请根据实际情况修改主应用程序中的更新检查逻辑和参数配置。

![支持我](https://gitee.com/xiaoqiangclub/xiaoqiangapps/raw/master/images/xiaoqiangclub_ad.png)