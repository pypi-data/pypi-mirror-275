from setuptools import setup, find_packages

setup(
    name='myinternshipcalculator2024',
    version='0.2.6',
    packages=find_packages(),
    install_requires=[],
    author='Abdallah Abdelsameia',
    author_email='aabdelsameia1@gmail.com',
    description='A simple internship hours calculator.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aabdelsameia1/myinternshipcalculator2024',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
