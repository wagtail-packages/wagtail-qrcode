#!/usr/bin/env python

import subprocess
from pathlib import Path


def make_sandbox():
    subprocess.call("wagtail start sandbox".split())
    clean_sandbox()


def delete_sandbox():
    subprocess.call("rm -rf sandbox".split())
    subprocess.call("rm manage.py".split())
    subprocess.call("rm db.sqlite3".split())


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
    urls_file = Path("sandbox/urls.py")
    urls_file.write_text(
        urls_file.read_text().replace(
            "from search import views as search_views", "from sandbox.search import views as search_views"
        )
    )
    file = Path("sandbox/settings/base.py")
    file.write_text(file.read_text().replace('"home",', '"sandbox.home",').replace('"search",', '"sandbox.search",'))
