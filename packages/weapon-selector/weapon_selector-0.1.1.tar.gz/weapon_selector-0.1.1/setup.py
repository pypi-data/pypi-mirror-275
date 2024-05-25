# setup.py
from setuptools import setup, find_packages

setup(
    name="weapon_selector",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "tk"
    ],
    entry_points={
        "console_scripts": [
            "weapon_selector=weapon_selector.app:main"
        ]
    },
    author="kakitaniakihiro",
    author_email="s2222010@stu.musashino-u.ac.jp",
    description="A simple Splatoon weapon selector assistant",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AkihiroKakitani/splaWeapon.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
