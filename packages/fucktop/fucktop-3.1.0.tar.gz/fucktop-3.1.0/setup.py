from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fucktop',
    version='3.1.0',
    description='一个免费而热搜工具(喜欢关注:python学霸微信公众号)',
    author='Python学霸',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='python@xueba.com',
    py_modules=['fucktop'],
    install_requires=['mechanicalsoup'],)