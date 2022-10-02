#!/usr/bin/env python

import subprocess
from pathlib import Path


def develop():
    if not Path("sandbox").exists():
        subprocess.call("wagtail start sandbox".split())
        clean_sandbox()
        configure_sandbox()
        copy_files()
    else:
        print("Sandbox already exists: run `clean` to delete it")


def clean():
    subprocess.call("rm -rf sandbox".split())
    subprocess.call("rm db.sqlite3".split())
    subprocess.call("rm -rf media".split())
    subprocess.call("rm -rf test-media".split())
    subprocess.call("rm -rf .tox".split())
    subprocess.call("rm -rf htmlcov".split())
    subprocess.call("rm .coverage".split())


def clean_sandbox():
    subprocess.call("rm -rf sandbox/.dockerignore".split())
    subprocess.call("rm -rf sandbox/Dockerfile".split())
    subprocess.call("rm -rf sandbox/requirements.txt".split())
    subprocess.call("mv sandbox/sandbox/settings sandbox".split())
    subprocess.call("mv sandbox/sandbox/static sandbox".split())
    subprocess.call("mv sandbox/sandbox/templates sandbox".split())
    subprocess.call("mv sandbox/sandbox/__init__.py sandbox".split())
    subprocess.call("mv sandbox/sandbox/urls.py sandbox".split())
    subprocess.call("mv sandbox/sandbox/wsgi.py sandbox".split())
    subprocess.call("rm -rf sandbox/sandbox".split())


def configure_sandbox():
    urls_file = Path("sandbox/urls.py")
    urls_file.write_text(
        urls_file.read_text().replace(
            "from search import views as search_views",
            "from sandbox.search import views as search_views",
        )
    )

    settings_file = Path("sandbox/settings/base.py")
    settings_file.write_text(
        settings_file.read_text()
        .replace('"home",', '"sandbox.home",')
        .replace('"search",', '"sandbox.search",')
    )
    settings_file.write_text(
        settings_file.read_text().replace(
            "INSTALLED_APPS = [", 'INSTALLED_APPS = ["wagtail_qrcode"] + ['
        )
    )
    urls_file = Path("sandbox/urls.py")
    urls_file.write_text(
        urls_file.read_text().replace(
            'path("search/", search_views.search, name="search"),',
            'path("search/", search_views.search, name="search"),\n    path("qr-code/", include("wagtail_qrcode.urls")),',  # noqa: E501
        )
    )


def copy_files():
    subprocess.call("cp bin/settings/dev.py sandbox/settings/dev.py".split())
    subprocess.call(
        "cp bin/migrations/0003_qrcodepage.py sandbox/home/migrations/0003_qrcodepage.py".split()  # noqa: E501
    )
    subprocess.call(
        "cp bin/migrations/0004_alter_qrcodepage_qr_code_svg_and_more.py sandbox/home/migrations/0004_alter_qrcodepage_qr_code_svg_and_more.py".split()  # noqa: E501
    )
    subprocess.call(
        "cp bin/migrations/0005_standardpage.py sandbox/home/migrations/0005_standardpage.py".split()  # noqa: E501
    )
    subprocess.call("cp bin/models/models.py sandbox/home/models.py".split())
    subprocess.call(
        "cp bin/templates/qr_code_page.html sandbox/home/templates/home/qr_code_page.html".split()  # noqa: E501
    )
    subprocess.call("mkdir -p sandbox/home/management/commands".split())
    subprocess.call("touch sandbox/home/management/__init__.py".split())
    subprocess.call("touch sandbox/home/management/commands/__init__.py".split())
    subprocess.call(
        "cp bin/commands/setup.py sandbox/home/management/commands/setup.py".split()
    )


def test_scripts():
    confirm = input(
        """DESTRUCTION IS IMMINENT!\n
        This will delete the sandbox directory and any data you have created.\n
        Continue? [y/N] """
    )
    result = []
    if confirm == "y":

        develop()

        if Path("sandbox").exists():
            result.append(True)
        else:
            result.append(False)

        clean()
        if not Path("sandboxs").exists():
            result.append(True)
        else:
            result.append(False)

        if all(result):
            print("SUCCESS! All tests passed")
        else:
            print("ERROR! Some tests failed")
            exit(1)

    else:
        print("ABORTED")
