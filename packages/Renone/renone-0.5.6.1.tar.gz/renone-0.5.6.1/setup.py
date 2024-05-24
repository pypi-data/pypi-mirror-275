from setuptools import setup, find_packages

setup(
    name='Renone',
    version='0.5.6.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'dcontrs = dcontrs.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.6',
)
