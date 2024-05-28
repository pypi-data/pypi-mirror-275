# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/27 19:00
# 文件名称： __init__.py
# 项目描述： 导入模块
# 开发工具： PyCharm
from importlib.resources import (as_file, files)
from XiaoqiangUpdater.updater import (updater,
                                      get_file_md5,
                                      updater_config_example,
                                      print_logo,
                                      print_usage)
from XiaoqiangUpdater.pack_to_exe import pack_to_exe

__version__ = '0.0.1'

__all__ = ['updater',
           'get_file_md5',
           'updater_config_example',
           'print_logo',
           'print_usage',
           'pack_to_exe']


def get_image_path(image_name):
    """
    获取包内图片的路径

    :param image_name: 图片文件名
    :return: 图片文件路径
    """
    with as_file(files('XiaoqiangUpdater') / f'img/{image_name}') as img_path:
        return str(img_path)


def ico_logo():
    """
    获取包内ico文件的路径

    :return: ico文件路径
    """
    return get_image_path('updater_logo.ico')


def png_logo():
    """
    获取包内logo文件的路径

    :return: logo文件路径
    """
    return get_image_path('updater_logo.png')
