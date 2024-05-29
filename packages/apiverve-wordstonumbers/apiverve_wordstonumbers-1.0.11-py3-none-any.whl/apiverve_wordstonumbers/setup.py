from setuptools import setup, find_packages

setup(
    name='apiverve_wordstonumbers',
    version='1.0.11',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Words to Numbers is a simple tool for converting words to numbers. It returns the words in numbers.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
