# _*_ coding : UTF-8 _*_
# 开发人员： Xiaoqiang
# 微信公众号: xiaoqiangclub
# 开发时间： 2024/5/27 17:48
# 文件名称： test_updater.py
# 项目描述： 测试
# 开发工具： PyCharm
from XiaoqiangUpdater import (updater, updater_config_example)


def test_updater():
    updater_config_example(save_path='updater_config.json')
    updater(config_path='updater_config.json')


if __name__ == '__main__':
    test_updater()
