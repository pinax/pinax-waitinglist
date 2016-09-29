import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()


setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a Django waiting list app",
    name="pinax-waitinglist",
    long_description=read("README.rst"),
    version="1.3.0",
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
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
