from setuptools import setup, find_packages


def read_file(filename: str) -> str:
    with open(filename, mode='r', encoding='utf-8') as input_file:
        return input_file.read()


setup(
    name='liuxiaojing',
    version='0.0.1',
    description='皛鲸的工具箱',
    author='liuxiaojing',
    author_email='lqxnjk@qq.com',
    url='https://xiaojing.cc/python',
    long_description=read_file("README.md"),  # 详细说明
    long_description_content_type="text/markdown",  # 详细说明使用标记类型
    classifiers=['Topic :: Software Development :: Libraries',
                 'Programming Language :: Python'],
    license='MIT',
    install_requires=[
        "pandas==1.3.5", "xlrd==1.2.0",
        "pymysql","requests", "openpyxl", "sqlalchemy", "pymongo"
    ],
    python_requires='>=3.7',
    packages=find_packages(),
    package_data={'': ['*.json', '*.ui', '*.svg', '*.qss', '*.xml', '*.png', '*.dot', '*.ini', '*.csv'],
                  'resources': ['*.json', '*.db', '*.xlsx', 'icons/*.*', 'private/*.*', 'templates/*.ini']},
)
