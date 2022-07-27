#!/usr/bin/env python

import subprocess
from pathlib import Path


def make_sandbox():
    subprocess.call("wagtail start sandbox".split())
    clean_sandbox()
    configure_sandbox()
    copy_files()


def delete_sandbox():
    subprocess.call("rm -rf sandbox".split())
    subprocess.call("rm manage.py".split())
    subprocess.call("rm db.sqlite3".split())
    subprocess.call("rm -rf media".split())


def clean_sandbox():
    subprocess.call("rm -rf sandbox/.dockerignore".split())
    subprocess.call("rm -rf sandbox/Dockerfile".split())
    subprocess.call("rm -rf sandbox/requirements.txt".split())
    subprocess.call("mv sandbox/manage.py .".split())
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
            "from search import views as search_views", "from sandbox.search import views as search_views"
        )
    )

    settings_file = Path("sandbox/settings/base.py")
    settings_file.write_text(
        settings_file.read_text().replace('"home",', '"sandbox.home",').replace('"search",', '"sandbox.search",')
    )
    settings_file.write_text(
        settings_file.read_text().replace("INSTALLED_APPS = [", 'INSTALLED_APPS = ["wagtail_qrcode"] + [')
    )


def copy_files():
    subprocess.call("cp bin/migrations/0003_qrcodepage.py sandbox/home/migrations/0003_qrcodepage.py".split())
    subprocess.call("cp bin/models/models.py sandbox/home/models.py".split())
    subprocess.call("cp bin/templates/qr_code_page.html sandbox/home/templates/home/qr_code_page.html".split())
    subprocess.call("mkdir -p sandbox/home/management/commands".split())
    subprocess.call("touch sandbox/home/management/__init__.py".split())
    subprocess.call("touch sandbox/home/management/commands/__init__.py".split())
    subprocess.call("cp bin/commands/setup.py sandbox/home/management/commands/setup.py".split())
    # subprocess.call("cp bin/settings/local.py sandbox/settings/local.py".split())
