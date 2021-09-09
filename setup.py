import setuptools

setuptools.setup(
    name=mypy_etherscan_api',
    version='0.8.0',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'examples.blocks', 'examples.transactions',  'etherscan'],
    url='https://github.com/Rose2161/mypy-etherscan-api',
    license='The Unlicense',
    author_changeS='Rose2161, 
    author_email='aisharose2161@gmail.com',
    description='Python Bindings to Etherscan.io API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
