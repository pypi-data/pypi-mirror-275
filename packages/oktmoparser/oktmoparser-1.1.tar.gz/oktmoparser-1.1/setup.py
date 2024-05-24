from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='oktmoparser',
    version='1.1',
    author='letimvkocmoc',
    author_email='letimvkocmoc@gmail.com',
    description='Simple and useful parser that helps you get actual All-Russian Classifier of Municipal Territories (OKTMO)',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/letimvkocmoc/oktmo-parser',
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='oktmo parser municipal territory classifier',
    project_urls={
        'GitGub': 'https://github.com/letimvkocmoc'
    },
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'oktmo-parser = oktmo_parser:main'
        ]
    }
)
