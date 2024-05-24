from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='my_data_preprocessor_mz',
    version='0.2.0',  # Initial development release
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'nltk',
        'scikit-learn'
    ],
    author=' Merve Demir, Zeynep Dagtekin',
    author_email='zeynep.dagtekin@stu.fsm.edu.tr',
    license='MIT',
    description='A comprehensive data preprocessing library for data engineering tasks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/meyvadem/my_data_preprocessor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
