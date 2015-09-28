# -*- coding: utf-8 -*-
import logging
import pkg_resources

__title__ = '{{ cookiecutter.repo_name }}'
__version__ = pkg_resources.get_distribution('{{cookiecutter.repo_name}}').version
__author__ = '{{ cookiecutter.full_name }}'

# the user should dictate what happens when a logging event occurs
logging.getLogger(__name__).addHandler(logging.NullHandler())
