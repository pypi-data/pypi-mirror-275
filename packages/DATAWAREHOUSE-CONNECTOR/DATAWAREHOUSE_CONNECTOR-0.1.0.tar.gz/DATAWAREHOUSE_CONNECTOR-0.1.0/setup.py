# setup.py
from setuptools import setup, find_packages

setup(
    name='DATAWAREHOUSE_CONNECTOR',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'psycopg2-binary',
        'redshift-connector',
        'snowflake-connector-python',
        'snowflake-sqlalchemy',
        'SQLAlchemy',
        'sqlalchemy-redshift',
        'urllib3'
    ],
    author='Poonam Saroj',
    author_email='poonam@coditation.com',
    description='A package for database session management',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Chandani7250/datawarehouse_connector',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
