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
    url="https://github.com/nickmoreton/wagtail-qrcode",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Framework :: Wagtail :: 3",
        "Framework :: Wagtail :: 4",
    ],
    install_requires=["Wagtail>=4.1", "PyQRCode>=1,<2"],
    extras_require={
        "testing": ["coverage"],
    },
    zip_safe=False,
)
