from setuptools import setup, find_packages

setup(
    name='pokerFunctions',
    version='0.2',
    packages=find_packages(),
    install_requires=[ ],
    include_package_data=True,
    description='A package for poker functions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jonah Aden',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/pokerFunctions',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
