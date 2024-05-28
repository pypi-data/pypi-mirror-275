# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/27 19:54
# 文件名称： test_pack_to_exe.py
# 项目描述： 测试
# 开发工具： PyCharm
from XiaoqiangUpdater import pack_to_exe

if __name__ == '__main__':
    pack_to_exe(main_file='test_updater.py', with_cmd_window=False, app_ico_logo=None)
