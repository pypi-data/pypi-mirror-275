from setuptools import setup, find_packages

setup(
    name='repartee',
    version='0.1.0',
    author='Matias Ceau',
    author_email='matias@ceau.net',
    description='A CLI tool to interface with multiple AI APIs for prompt-response handling.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/matias-ceau/repartee',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.25.1',
        'PyYAML>=5.4.1',
        'prompt_toolkit>=3.0.18',
        'setuptools>=58.0.0',
        'wheel>=0.36.2',
        'twine>=3.4.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'repartee=repartee.cli:main',
        ],
    },
    project_urls={
        'Bug Tracker': 'https://github.com/matias-ceau/repartee/issues',
        'Source Code': 'https://github.com/matias-ceau/repartee',
    },
)