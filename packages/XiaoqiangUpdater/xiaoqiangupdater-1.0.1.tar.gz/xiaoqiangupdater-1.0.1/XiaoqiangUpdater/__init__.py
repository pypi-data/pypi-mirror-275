from importlib.resources import (as_file, files)
from XiaoqiangUpdater.updater import (updater,
                                      get_file_md5,
                                      updater_config_example,
                                      print_logo,
                                      print_usage,
                                      handle_arguments)
from XiaoqiangUpdater.pack_to_exe import pack_to_exe

__version__ = '1.0.1'

__all__ = ['updater',
           'get_file_md5',
           'updater_config_example',
           'print_logo',
           'print_usage',
           'handle_arguments',
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


print_logo()
