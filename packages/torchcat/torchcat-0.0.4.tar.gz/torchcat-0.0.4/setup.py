from setuptools import setup

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='torchcat',
    version='0.0.4',
    author='kaiyu',
    author_email='2971934557@qq.com',
    license='GPL',
    url='https://pypi.org/project/torchcat/',
    description='用于简化 torch 模型训练的工具',
    long_description=long_description,
    packages=['torchcat'],
    install_requires=['numpy', 'torchsummary'],
)

'''
python -m build

python -m twine upload --repository pypi dist/*
'''
