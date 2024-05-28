from setuptools import setup, find_packages
import codecs


# 从 requirements.txt 文件读取依赖
def read_requirements():
    with codecs.open('requirements.txt', 'r', encoding='utf-8') as f:
        return f.read().splitlines()


setup(
    name='XiaoqiangUpdater',  # 项目名称
    version='1.0.0',
    description='A general purpose program upgrade tool',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='XiaoqiangClub',
    author_email='xiaoqiangclub@hotmail.com',
    url='https://github.com/xiaoqiangclub/XiaoqiangUpdater',  # 更新URL
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'updater=XiaoqiangUpdater.updater:handle_arguments',
        ],
    },
    python_requires='>=3.6',
    include_package_data=True,
)
