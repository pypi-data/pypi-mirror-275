from setuptools import setup, find_packages

setup(
    name='data_cleaner_byzahid',
    version='0.1.0',
    author='Zahid Esad Baltacı',
    author_email='zahid.bltci@gmail.com',
    description='A comprehensive Python library for data preprocessing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zahidesad/Data-Cleaner-For-Movie-Recommendation',
    download_url='https://github.com/zahidesad/Data-Cleaner-For-Movie-Recommendation/archive/refs/tags/0.1.0.tar.gz',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'nltk',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
