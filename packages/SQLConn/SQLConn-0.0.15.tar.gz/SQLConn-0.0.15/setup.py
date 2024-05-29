from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='SQLConn',
    version='0.0.15',
    description='This package facilitates easy SQL database integration.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='janyoungjin',
    install_requires=[
        'pandas',
        'sqlalchemy',
        'pymysql',
        'pymssql',
        'psycopg2-binary'
    ],
    packages=find_packages(),
    url='https://github.com/janyoungjin/SQLConn',
    keywords=['mysql', 'postgresql', 'sqlite', 'mssql', 'sql'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
