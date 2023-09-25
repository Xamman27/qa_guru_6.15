import pytest
from selene.support.shared import browser
from selene import be, have
"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""


@pytest.fixture(autouse=False, scope='function', params=[(2048, 1080), (1920, 1080), (1024, 768)])
def desktop_browser(request):
    browser.config.base_url ='https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


@pytest.fixture(autouse=False, scope="function",params=[(360, 640), (375, 812)])
def mobile_browser(request):
    browser.config.base_url = 'https://github.com'
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]
    yield
    browser.quit()


def test_github_desktop(desktop_browser):
    browser.open('/')
    browser.element('[class="position-relative mr-lg-3 d-lg-inline-block"]').click()
    browser.element(".auth-form-header").should(be.visible)


def test_github_mobile(mobile_browser):
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element('[href="/login"]').click()
    browser.element(".auth-form-header").should(have.exact_text("Sign in to GitHub"))