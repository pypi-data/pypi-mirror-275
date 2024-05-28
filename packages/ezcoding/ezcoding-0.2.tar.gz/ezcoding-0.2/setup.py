# coding: utf-8

from setuptools import setup

setup(
    name='ezcoding',
    version='0.2',
    packages=['ezcoding', 'ezcoding.generators', 'ezcoding.ui', 'ezcoding_cli'],
    url='https://github.com/zhuuuoyue/ezcoding',
    license='MIT',
    author='zhuoy',
    author_email='zhuoyue_cn@yeah.net',
    description='Eazy coding',
    install_requires=['pyside6'],
    entry_points={
        'console_scripts': [
            'ezc = ezcoding_cli.cli:main'
        ]
    }
)
