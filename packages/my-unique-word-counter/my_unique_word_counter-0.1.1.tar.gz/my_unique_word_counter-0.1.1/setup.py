from setuptools import setup, find_packages

setup(
    name='my_unique_word_counter',
    version='0.1.1',
    packages=find_packages(),
    author='Izu Hayato',
    author_email='hayato.0210.0210@gmail.com',
    description='A package to count word frequencies in a text with stopword removal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/izzzuuuuuuuuu/word_counter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
