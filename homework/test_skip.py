from selene.support.shared import browser
from selene import be, have
import pytest


"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""


def is_desktop_device(width, height):
    if width > height:
        return True
    else:
        return False

@pytest.fixture(
    autouse=True,
    scope="function",
    params=[
        (360, 640),
        (375, 812),
        (2048, 1080),
        (1920, 1080),
        (1024, 768)
    ]
)
def browser_setting(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


def test_github_desktop(browser_setting):
    if is_desktop_device(browser.config.window_width, browser.config.window_height) is False:
        pytest.skip("Test for mobile")
    browser.open('/')
    browser.element('[class="position-relative mr-lg-3 d-lg-inline-block"]').click()
    browser.element(".auth-form-header").should(be.visible)


def test_github_mobile(browser_setting):
    if is_desktop_device(browser.config.window_width, browser.config.window_height):
        pytest.skip("Test for desktop")
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element('[href="/login"]').click()
    browser.element(".auth-form-header").should(have.exact_text("Sign in to GitHub"))