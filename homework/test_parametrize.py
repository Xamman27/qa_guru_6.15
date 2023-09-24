"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest


@pytest.fixture()
def browser():
    pass


def test_github_desktop(browser):
    pass


def test_github_mobile(browser):
    pass
