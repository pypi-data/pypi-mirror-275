# from setuptools import setup, find_packages

# setup(
#     name='splatoon-weapon-selector',      # パッケージの名前（PyPIに登録される名前）
#     version='1.0.0',                      # パッケージのバージョン番号
#     packages=['splatoon_weapon_selector'], # 手動でパッケージを指定
#     install_requires=['tkinter'],
#     entry_points={                        # コマンドラインスクリプトのエントリーポイント
#         'console_scripts': [
#             'splatoon-weapon-selector = splatoon_weapon_selector.main:main'
#         ],
#     },
#     author='kakitaniakihiro',                   # 作者名
#     author_email='s2222010@stu.musashino-u.ac.jp',  # 作者のメールアドレス
#     description='A Splatoon weapon selector GUI application',  # パッケージの簡潔な説明
#     url='https://github.com/AkihiroKakitani/splaWeapon.git',  # パッケージのURL
#     classifiers=[                         # PyPIでの分類
#         'Programming Language :: Python :: 3',
#         'License :: OSI Approved :: MIT License',
#         'Operating System :: OS Independent',
#     ],
# )

# from setuptools import setup, find_packages

# setup(
#     name='splatoon-weapon-selector',
#     version='0.1.0',
#     description='splatoon-weapon-selector',
#     long_description=open('README.md').read(),
#     long_description_content_type='text/markdown',
#     url='https://github.com/AkihiroKakitani/splaWeapon.git',  # リポジトリのURL
#     author='kakitaniakihiro',
#     author_email='s2222010@stu.musashino-u.ac.jp',
#     license='MIT',
#     packages=find_packages(),
#     classifiers=[
#         'Development Status :: 3 - Alpha',
#         'Intended Audience :: Developers',
#         'Topic :: Games/Entertainment',
#         'License :: OSI Approved :: MIT License',
#         'Programming Language :: Python :: 3.7',
#         'Programming Language :: Python :: 3.8',
#         'Programming Language :: Python :: 3.9',
#     ],
#     python_requires='>=3.7',
# )

from setuptools import setup

setup(
    name='weapon-selector',
    version='0.1',
    py_modules=['weapon-selector'],
    install_requires=[],
)