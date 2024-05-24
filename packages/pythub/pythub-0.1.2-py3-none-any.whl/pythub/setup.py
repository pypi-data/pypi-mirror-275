from setuptools import setup, find_packages

setup(
    name='pythub',
    version='0.1.2',
    author='MOHAMED RAGAB ABDELFATTAH ABDELFADEEL-MHD Alhabeb Alshalah-AHMED EMAD ELSAYED MOHAMED ABDELFATTAH',
    author_email='mehmetrecep650@gmail.com',
    description='A comprehensive Python library for data preprocessing tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mehmetrecep/pythub',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
