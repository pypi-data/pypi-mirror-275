# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/27 19:17
# 文件名称： pack_to_exe.py
# 项目描述： 将updater打包成exe
# 开发工具： PyCharm
import os
import subprocess
import urllib.request

DEFAULT_ICO_LOGO_URL = "https://gitee.com/xiaoqiangclub/xiaoqiangapps/raw/master/pypi/updater/app_logo.ico"


def download_file(url, path):
    """
    下载文件
    :param url: 文件URL
    :param path: 保存路径
    """
    try:
        urllib.request.urlretrieve(url, path)
        print(f"文件下载成功：{path}")
    except Exception as e:
        print(f"文件下载失败：{e}")


def pack_to_exe(main_file: str = "updater/updater.py", with_cmd_window: bool = False, app_ico_logo: str = None):
    """
    打包程序为exe文件

    :param main_file: updater入口文件
    :param with_cmd_window: 是否带终端窗口
    :param app_ico_logo: logo文件路径
    :return:
    """
    if not app_ico_logo:
        app_ico_logo = os.path.join(os.getcwd(), 'temp', 'app_logo.ico')
        if not os.path.exists(app_ico_logo):
            os.makedirs(os.path.join(os.getcwd(), 'temp'), exist_ok=True)
            # 下载app_logo.ico文件到temp目录
            download_file(DEFAULT_ICO_LOGO_URL, app_ico_logo)

    with_cmd = '' if with_cmd_window else '--noconsole'

    # 构建打包命令
    command = [
        'pyinstaller',
        '--onefile',
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
