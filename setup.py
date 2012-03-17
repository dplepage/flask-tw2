"""
Flask-TW2
---------

Flask support for the TW2.

Links
`````

* `documentation <http://packages.python.org/Flask-TW2>`_

"""

from setuptools import setup

setup(
    name='Flask-TW2',
    version='0.1',
    url='http://github.com/dplepage/flask-tw2',
    license='BSD',
    author='Dan Lepage',
    author_email='dplepage@gmail.com',
    maintainer='Dan Lepage',
    maintainer_email='dplepage@gmail.com',
    description='TW2 support for Flask',
    long_description=__doc__,
    pymodules=['flask_tw2'],
    test_suite='nose.collector',
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'tw2.core',
    ],
    tests_require=[
        'nose',
        'tw2.forms'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
