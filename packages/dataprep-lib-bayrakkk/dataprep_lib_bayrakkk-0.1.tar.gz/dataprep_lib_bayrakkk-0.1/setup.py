from setuptools import setup, find_packages

setup(
    name='dataprep_lib_bayrakkk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk'
    ],
    author='Enes Bayraker, Fatma Nur Bargan',
    author_email='enes.bayraker@stu.fsm.edu.tr, fatmanur.bargan@stu.fsm.edu.tr',
    description='A comprehensive Python library for data preprocessing',
    url='https://github.com/EnesBayraker/data_preprocessing_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
