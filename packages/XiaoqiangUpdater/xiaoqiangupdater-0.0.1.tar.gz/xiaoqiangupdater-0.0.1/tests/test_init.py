# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/28 11:04
# 文件名称： test_init.py
# 项目描述： 测试
# 开发工具： PyCharm

if __name__ == '__main__':
    import XiaoqiangUpdater
    from XiaoqiangUpdater import *

    print_logo()
    print_usage()
    print(XiaoqiangUpdater.__version__)
    print(get_file_md5(r'D:\001_MyArea\002_MyCode\001_PythonProjects\pypi\xiaoqiangupdater\XiaoqiangUpdater\dist\updater.exe'))
