from setuptools import setup, find_packages

setup(
    name='csv_summary',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'csv_summary=csv_summary.summary:summarize_csv',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='指定したCSVファイルの統計情報を生成するパッケージ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/csv_summary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
