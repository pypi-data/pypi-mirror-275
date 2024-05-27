from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='torchcat',
    version='0.0.8',
    author='KaiYu',
    author_email='2971934557@qq.com',  # 作者邮箱
    url='https://gitee.com/kkkaiyu/torchcat',  # 项目主页
    description='TorchCat 是用于封装 PyTorch 模型的工具',  # 简单描述
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    install_requires=['torch', 'torchvision', 'torchsummary', 'numpy'],
    # packages=['torchcat'],                 # 包
    python_requires='>=3.9',
)

'''
python -m build

python -m twine upload --repository pypi dist/* 
'''
