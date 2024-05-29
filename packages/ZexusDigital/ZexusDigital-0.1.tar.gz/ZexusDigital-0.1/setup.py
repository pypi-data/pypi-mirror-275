from setuptools import setup, find_packages

setup(
    name='ZexusDigital',
    version='0.1',
    packages=find_packages(include=['zexusdigital', 'zexusdigital.*']),
    install_requires=[
        'requests',
        'loguru',
        'jmespath',
    ],
    author='Zexus',
    author_email='zexusdigital@zexusdigital.com',
    description='Instagram Scraping',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ZexusDigital/instagram-scraper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
