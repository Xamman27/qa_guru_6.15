import random

import pytest
import time

# pytestmark = pytest.mark.skip(reason="TASK-1234 Тест нестабильный потому что время от времени не хватает таймаута")


@pytest.fixture(scope="session")
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


@pytest.fixture()
def user(browser):
    return random.randint(0, 100)


@pytest.mark.fast
@pytest.mark.skip(reason="TASK-1234 Тест нестабильный потому что время от времени не хватает таймаута")
def test_first(browser):
    time.sleep(1)


@pytest.mark.slow
@pytest.mark.usefixtures("browser")
@pytest.mark.skip("TASK-123 Еще не реализован")
def test_second(user):
    time.sleep(5)


is_macos = True


@pytest.fixture()
def is_macos():
    return True


# @pytest.mark.skipif(is_macos)
def test_third(is_macos):
    if is_macos:
        pytest.skip(reason="Не запускается на macos")


# @pytest.mark.xfail(reason="протсо потому что")
def test_fail():
    user1 = random.randint(0, 100)
    user2 = random.randint(0, 100)

    assert user1 <= 100
    assert user2 <= 100
    try:
        assert user1 == user2
    except AssertionError:
        pytest.xfail("TASK-1234")
