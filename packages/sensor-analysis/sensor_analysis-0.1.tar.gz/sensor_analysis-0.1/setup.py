from setuptools import setup, find_packages

setup(
    name='sensor_analysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'numpy'
    ],
    author='Mohammed Adams',
    author_email='moadams847@gmail.com',
    description='A package for analyzing low-cost sensor and reference data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/moadams847/sensor_analysis',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)
