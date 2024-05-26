from setuptools import setup, find_packages

setup(
    name='pymail2',
    version='0.1.0',
    author='Avinash Negi',
    author_email='avinash.negi2194@gmail.com',
    description='This is most easiest way to send email using smtp',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/oakdatamechanic/pymail',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
)
