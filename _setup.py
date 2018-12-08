from setuptools import setup

setup(
    name='Flask-Exchange',
    version='0.0.1',
    packages=['flask_exchange'],
    url='https://github.com/jscurtu/flask-exchange',
    license='MIT',
    author='Jason Scurtu',
    author_email='jscurtu@gmail.com',
    description='Exchange support for Flask using ExchangeLib',
    keywords=['exchange', 'exchangelib', 'email'],
    install_requires=['flask>=0.10.1', 'exchangelib>=1.12.0', 'urllib3'],
    data_files=[('', ['LICENSE'])],
    classifiers=[
        'Framework :: Flask',
        'Topic :: Office/Business :: Groupware',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
