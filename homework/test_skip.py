"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest


@pytest.fixture()
def browser():
    pass


def test_github_desktop(browser):
    pass


def test_github_mobile(browser):
    pass
