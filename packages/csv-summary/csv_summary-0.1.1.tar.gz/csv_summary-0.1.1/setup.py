from setuptools import setup, find_packages

setup(
    name='csv_summary',
    version='0.1.1',  # バージョン番号を更新
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'csv_summary=csv_summary.summary:summarize_csv',
        ],
    },
    author='pika8911',
    author_email='s2122043@stu.musashino-u.ac.jp',
    description='指定したCSVファイルの統計情報を生成するパッケージ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pika8911/csv_summary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
