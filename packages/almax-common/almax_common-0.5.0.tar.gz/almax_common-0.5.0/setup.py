from setuptools import setup, find_packages

setup(
    name='almax_common',
    version='0.5.0',
    description='A common library with some of my implementations',
    long_description='test',
    long_description_content_type='text/markdown',
    author='AlMax98',
    author_email='alihaider.maqsood@gmail.com',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'logging',
        'subprocess',
        'reportlab',
        'threading',
        'datetime',
        'os',
        'sys'
    ],
);