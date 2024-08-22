import pytest
from prac import search_gaming_monitor


@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_search_gaming_monitor():

    page_content = search_gaming_monitor()

    # Assert that "Gaming Monitor" is in the page content
    assert "Gaming Monitor" in page_content, "Page does not contain 'Gaming Monitor'"
