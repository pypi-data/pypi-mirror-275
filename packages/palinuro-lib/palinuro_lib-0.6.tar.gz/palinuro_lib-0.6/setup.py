from setuptools import setup, find_packages

setup(
    name='palinuro_lib',
    version='0.6',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.8.4',
        'matplotlib-inline==0.1.7',
        'numpy==1.26.4',
        'pandas==2.2.2',
        'scipy==1.13.0',
       ' seaborn==0.13.2',
    ],
    author='Vincenzo Brigandi',
    author_email='brigandi.vincenzo@yahoo.com',
    description='A library for trading in a Macro Hedge Fund',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/vcnzbrgd/palinuro_lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
