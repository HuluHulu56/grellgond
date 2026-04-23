from setuptools import setup, find_packages

setup(
    name='grellgond',
    version='0.1.2', 
    description='Official library for ℷ (The Grellgond mathematical constant)',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Simon & Viliam',
    url='https://github.com/HuluHulu56/grellgond',
    packages=find_packages(),
    install_requires=['sympy'],
    entry_points={
        'console_scripts': [
            'grellgond=grellgond.cli:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
