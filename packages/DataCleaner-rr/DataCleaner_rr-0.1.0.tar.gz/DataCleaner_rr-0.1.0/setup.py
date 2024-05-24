# setup.py
from setuptools import setup, find_packages

setup(
    name='DataCleaner_rr',
    version='0.1.0',
    description='A comprehensive data preprocessing library for data cleaning, transformation, and manipulation',
    author='Rana Güngör',
    author_email='rana.gungor@stu.fsm.edu.tr',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
