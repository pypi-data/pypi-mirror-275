# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

# プロジェクトのルートディレクトリを取得
HERE = os.path.abspath(os.path.dirname(__file__))

# README.mdの内容を読み込む
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='wellbeing_calculator',
    version='0.4',  # バージョン番号を更新
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'wellbeing_calculator=wellbeing_calculator.calculator:main',
        ],
    },
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your-email@example.com',
    description='A tool to evaluate the impact of social media usage on personal wellbeing and lifestyle habits',
    url='https://github.com/yourusername/wellbeing_calculator',  # プロジェクトのリポジトリURL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
)

