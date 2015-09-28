# -*- coding: utf-8 -*-
import pytest

from {{cookiecutter.repo_name}}.factory import create_app
from {{cookiecutter.repo_name}}.settings import TestConfig


@pytest.fixture
def app(request):
    app = create_app(config_obj=TestConfig)
    return app
