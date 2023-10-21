import setuptools

setuptools.setup(
    name='py_etherscan_api',
    version='0.9.0',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'examples.blocks', 'examples.transactions',  'etherscan'],
    url='https://github.com/rose2161/py-etherscan-api',
    license='Gnup',
    author='aisha redl',
    author_email='aisharose2161@gmail.com',
    description='Python Bindings to Etherscan.io API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
