from setuptools import setup, find_packages

setup(
    name='eras',
    version='0.4.8',
    include_package_data=True,
    packages=find_packages(include=["eras", "eras.*"]),
    package_data={
        '': ['*.txt', '*.rst'],
        'eras': ['*.md'],
    },
    install_requires=[
        'openai==1.26.0',
        'keyboard==0.13.5',
        'python-dotenv==1.0.0',
        'asyncio==3.4.3',
        'InquirerPy==0.3.4',
        'colorama==0.4.6'
    ],
    entry_points={
        'console_scripts': [
            'eras=eras.main:main',
        ],
    },
    author='Jason McAffee',
    author_email='jasonlmcaffee@gmail.com',
    description='A terminal command library that provides a Natural Language Interface for running shell commands.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jasonmcaffee/eras',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
