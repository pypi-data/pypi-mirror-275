from setuptools import setup, find_packages

setup(
    name='data_preprocessing_library_sevvalcucuk_asudesozcu',
    version='1.1.6',
    description='A comprehensive toolkit for data processing including handling dates, encoding categorical variables, handling missing values, outliers, and text cleaning.',
    author='Şevval Cücük, Asude Sözcü',
    author_email='sevcck@gmail.com sozcuasude@gmail.com',
    url='https://github.com/clavves/data_preprocessing_library_sevvalcucuk_asudesozcu',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.1.0',
        'numpy>=1.19.0',
        'python-dateutil>=2.8.0',
        'scikit-learn>=0.24.0',
        'nltk>=3.5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
    ],
    python_requires='>=3.7',
    keywords='data processing, data cleaning, date handling, encoding, imputation, outlier handling, text cleaning',
)