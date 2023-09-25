from selene.support.shared import browser
from selene import be, have
import pytest
"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""


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


@pytest.mark.parametrize('browser_setting', [(2048, 1080), (1920, 1080), (1024, 768)], indirect=True)
def test_github_desktop():
    browser.open('/')
    browser.element('[class="position-relative mr-lg-3 d-lg-inline-block"]').click()
    browser.element(".auth-form-header").should(be.visible)


@pytest.mark.parametrize('browser_setting', [(360, 640), (375, 812)], indirect=True)
def test_github_mobile():
    browser.open('/')
    browser.element('.flex-1 button').click()
    browser.element('[href="/login"]').click()
    browser.element(".auth-form-header").should(have.exact_text("Sign in to GitHub"))