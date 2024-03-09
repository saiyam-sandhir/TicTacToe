from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='TicTacToe',
    version='0.1',
    maintainer='Saiyam Jain, Arpit Baranwal',
    maintainer_email='saiyamsandhir@gmail.com, ',
    description='A Tic Tac Toe game',
    url='https://github.com/saiyam-sandhir/TicTacToe.git',
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.11',
    ],
)
