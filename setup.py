#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup

from wagtail_qrcode import __version__

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtail-qrcode",
    version=__version__,
    description="Create a QR code that can be used to link to a wagtail page",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nick Moreton",
    author_email="nickmoreton@me.com",
    url="",
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 3",
    ],
    install_requires=["Django>=3.2", "Wagtail>=3.0", "PyQRCode>=1.2.1"],
    extras_require={
        "testing": [],
    },
    zip_safe=False,
)
