# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/27 19:17
# 文件名称： pack_to_exe.py
# 项目描述： 将updater打包成exe
# 开发工具： PyCharm
import os
import subprocess
from importlib.resources import as_file, files


def pack_to_exe(main_file: str = None, with_cmd_window: bool = False, app_ico_logo: str = None, onefile: bool = True):
    """
    打包程序为exe文件

    :param main_file: updater入口文件
    :param with_cmd_window: 是否带终端窗口
    :param app_ico_logo: logo文件路径
    :param onefile: 是否将程序打包成单一的exe文件，默认是
    :return:
    """
    # 如果没有设置 main_file，默认为 'XiaoqiangUpdater/updater.py'
    if main_file is None:
        with as_file(files('XiaoqiangUpdater') / 'updater.py') as default_main_file:
            main_file = str(default_main_file)

    # 如果没有设置 logo 文件路径，使用模块内部的默认图标
    if not app_ico_logo:
        with as_file(files('XiaoqiangUpdater') / 'img/updater_logo.ico') as default_ico_logo:
            app_ico_logo = str(default_ico_logo)

    # 设置是否带终端窗口
    with_cmd = '' if with_cmd_window else '--noconsole'

    # 设置是否将程序封装成单一的exe文件
    onefile_option = '--onefile' if onefile else '--onedir'

    # 构建打包命令
    command = [
        'pyinstaller',
        onefile_option,
        with_cmd,
        '--distpath', 'dist',
        '--name', 'updater',
        '--icon', app_ico_logo,
        main_file
    ]

    # 使用Popen类执行命令，并实时打印输出
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        print(line, end="")

    process.stdout.close()
    process.wait()

    # 打开exe文件所在目录
    try:
        os.startfile(os.path.join(os.getcwd(), 'dist'))
        print("打包完成，请查看dist目录")
    except Exception as e:
        print(f"打开dist目录失败：{e}")


if __name__ == '__main__':
    # 示例调用
    pack_to_exe()
