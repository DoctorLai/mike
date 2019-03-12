from setuptools import setup, find_packages

setup(
    name='drugwars_mike',
    version='0.0.9',
    packages=find_packages(),
    url='http://github.com/emre/mike',
    license='MIT',
    author='emre yilmaz',
    author_email='mail@emreyilmaz.me',
    description='A discord bot to notify battles',
    entry_points={
        'console_scripts': [
            'mike = mike.main:main',
        ],
    },
    install_requires=["dataset", "discord.py", "aioredis"]
)