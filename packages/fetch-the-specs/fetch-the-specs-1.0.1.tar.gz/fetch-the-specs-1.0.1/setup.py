from setuptools import setup, find_packages

setup(
    name='fetch-the-specs',
    version='1.0.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'fetch-the-specs=fetch_the_specs:main'
        ]
    },
    author='Ibrahim Hasnat',
    description='A command-line tool to report system information in a colorful format.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    url='https://github.com/ibrahimhasnat/fetch-the-specs/'
)