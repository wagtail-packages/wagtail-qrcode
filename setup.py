#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="wagtail-qrcode",
    version="0.1.0",
    description="Create a QR code that can be used to link to a wagtail page",
    long_description="### A long description",
    long_description_content_type="text/markdown",
    author="Nick Moreton",
    author_email="nickmoreton@me.com",
    url="https://github.com/nickmoreton/wagtail-qrcode",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 3",
    ],
    install_requires=["Django>=3.2", "Wagtail>=3.0", "PyQRCode>=1.2.1"],
    extras_require={
        "testing": [],
    },
    zip_safe=False,
)
