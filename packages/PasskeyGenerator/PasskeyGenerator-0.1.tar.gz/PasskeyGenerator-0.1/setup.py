from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='PasskeyGenerator',
    version='0.1',
    author='chadee',
    author_email='esurginet2011@gmail.com',
    description='This is module generates passwords',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='password generator',
    python_requires='>=3.9'
)
