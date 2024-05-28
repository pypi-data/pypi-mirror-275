from setuptools import setup
import re, os

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)

with open('auto/__init__.py', 'r',encoding='utf-8') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
    
setup(
    name='HappyLife',
    version=version,
    packages=['auto'],
    author="宇宙中的塵埃",
    author_email="yqnacfmh9@gmail.com",
    description="圖色識別，自動操作滑鼠/鍵盤(可後臺運行)，將一切重複的事，抽象為函數，自動運行。\n從今天開始，拒絕做無聊的事情，做自己想做的事吧~",
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        'numpy==1.23.1',
        'opencv-python==4.6.0.66',
        'Pillow==9.2.0',
        'pywin32==304'
    ]
)
