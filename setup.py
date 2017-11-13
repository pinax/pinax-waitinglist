from setuptools import find_packages, setup

LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/blank.svg
    :target: https://pypi.python.org/pypi/pinax-waitinglist/

=================
Pinax Waiting List
=================

.. image:: https://img.shields.io/pypi/v/waitinglist.svg
    :target: https://pypi.python.org/pypi/waitinglist/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/waitinglist/

.. image:: https://img.shields.io/circleci/project/github/pinax/waitinglist.svg
    :target: https://circleci.com/gh/pinax/waitinglist
.. image:: https://img.shields.io/codecov/c/github/pinax/waitinglist.svg
    :target: https://codecov.io/gh/pinax/waitinglist
.. image:: https://img.shields.io/github/contributors/pinax/waitinglist.svg
    :target: https://github.com/pinax/waitinglist/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/waitinglist.svg
    :target: https://github.com/pinax/waitinglist/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/waitinglist.svg
    :target: https://github.com/pinax/waitinglist/pulls?q=is%3Apr+is%3Aclosed

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/


``pinax-waitinglist`` is a waiting list app for Django sites.


Supported Django and Python Versions
------------------------------------

* Django 1.8, 1.10, 1.11, and 2.0
* Python 2.7, 3.4, 3.5, and 3.6
"""


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a Django waiting list app",
    name="pinax-waitinglist",
    long_description=LONG_DESCRIPTION,
    version="1.3.1",
    url="http://github.com/pinax/pinax-waitinglist/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "waitinglist": [
            "templates/waitinglist/_list_signup.html",
            "templates/waitinglist/_success.html"
        ]
    },
    test_suite="runtests.runtests",
    tests_require=[
        "django-test-plus>=1.0.12",
    ],
    install_requires=[
    ],    
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)